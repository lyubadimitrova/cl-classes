import bag_of_wording
import argparse
from collections import Iterable, OrderedDict


def find_most_similar(bags_of_words):
    
    biggest_overlap = [0, (0, 0)]
    
    keys = list(bags_of_words)      
    
    for i in range(len(keys) - 1):
        for j in range(i + 1, len(keys)):
            seq1 = bags_of_words[keys[i]]
            seq2 = bags_of_words[keys[j]]
            
            try:
                norm_overlap = len(seq1.intersection(seq2)) / max(len(seq1), len(seq2))
            except ZeroDivisionError:           # in case the BoW-extraction left an empty set
                norm_overlap = 0
                
            if norm_overlap > biggest_overlap[0]:
                biggest_overlap[0] = norm_overlap
                biggest_overlap[1] = (keys[i], keys[j])
        
    return biggest_overlap
    

def word_overlap_clustering(queries, bags_of_words, overlap_threshold):
    
    for query in queries:
        
        bows_for_query = {k: v for k, v in bags_of_words.items() if k.split('.')[0] == query}
        bows_for_query = OrderedDict(sorted(bows_for_query.items(), key=lambda t: t[0]))    # ensures stability of the clustering through multiple runs
        
        
        while True:
            
            overlap, to_merge = find_most_similar(bows_for_query)
            
            if overlap <= overlap_threshold:
                yield bows_for_query.keys()
                break
            
            bows_for_query[to_merge] = bows_for_query[to_merge[0]].union(bows_for_query[to_merge[1]])
            
            bows_for_query.pop(to_merge[0])
            bows_for_query.pop(to_merge[1])
  
        

def flatten(sequence):
    """
    Since the clustering produces hierarchical clusters in the form ((((1,2),3),(4,5)),6), a 'flattening'
    is needed in order to write the desired output.
    
    ((((1,2),3),(4,5)),6) -> (1, 2, 3, 4, 5, 6)
    """
    for elm in sequence:
        if isinstance(elm, Iterable) and not isinstance(elm, str):
            yield from flatten(elm)
        else:
            yield elm
            

def write_output(clustering, filename):
    with open(filename, 'w') as f:
        f.write('subTopicID\tresultID\n')
        for query in clustering:
            for i, cluster in enumerate(query):
                for element in cluster:
                    f.write('{}.{}\t{}\n'.format(element.split('.')[0], i, element))
                    
                    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--input_dir', help='Dataset directory, containing the topics.txt and results.txt files.')
    parser.add_argument('-o', '--output_file', help='Output file name (if need be with an *existing* directory).', default="output.txt")
    parser.add_argument('-t', '--overlap_threshold', type=float, help='The overlap threshold of the clustering algorithm (ignored if -b specified).', default=0.02)
    parser.add_argument('-b', '--baseline', help='Produces the simplified system output, with overlap threshold = 0 and a TreeTagger file from the input directory.', action="store_true")
    
    args = parser.parse_args()
        
    queries = bag_of_wording.extract_queries(args.input_dir + "/topics.txt")
    if args.baseline:
        bows = bag_of_wording.extract_bow_treetagger(queries, args.input_dir + "/tagged.txt")
        overlap_threshold = 0
    else:
        bows = bag_of_wording.extract_bow(queries, args.input_dir + "/results.txt")
        overlap_threshold = args.overlap_threshold
    
    
    final_clustering = []
    
    for clustering in word_overlap_clustering(queries, bows, overlap_threshold):
        clustering_for_query = []
        for cl in clustering:
            if not isinstance(cl, str):
                clustering_for_query.append(list(flatten(cl)))
        
        final_clustering.append(clustering_for_query)
        
       
    write_output(final_clustering, args.output_file)
    