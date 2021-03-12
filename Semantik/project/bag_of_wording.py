"""This module does the necessary preprocessing of the data.
"""


def extract_queries(filename):
    queries = {}
    
    with open(filename, 'r') as f:
        
        next(f)                 #skip file header
        
        for line in f:
            l = line.rstrip().split("\t")
            queries[l[0]] = [word for word in l[1].split("_")]
            queries[l[0]].append(l[1])
    
    return queries


def extract_bow(queries, filename):
    """
    Creates a dictionary out of the search results file, 
    where the key is the snippet ID (e.g '45.13'), and the value a set representing the snippet text as a bag-of-words.
    """
    import spacy
    
    results = {}
    special_stopwords = {'wikipedia', 'free', 'encyclopedia', 'urban', 'dictionary'}
    
    model = spacy.load("en")

    
    with open(filename, encoding='utf-8') as reader:
        
        next(reader)        #skip file header
        
        for line in reader:
            
            ID, _, text = line.strip().split("\t", 2)
            results[ID] = set()
            topic = queries[ID.split('.')[0]]
            
            snippet = model(text)
            
            for w in snippet:
                
                if w.tag_.startswith("N") and w.is_alpha and w.text.lower() not in topic and not w.is_stop and w.text.lower() not in special_stopwords:
                    results[ID].add(w.lemma_.lower())
                
            
            for np in snippet.noun_chunks:
                
                while len(np) > 1 and np[0].tag_ not in ('JJ', 'JJS', 'JJR'):
                    np = np[1:]
                    
                np = '_'.join([w.lemma_ for w in np if w.text.lower() not in special_stopwords]).lower()
                    
                if np.count("_") == 1 and np not in topic and np.replace('_', '').isalpha():
                    results[ID].add(np)
            
    return results
        

def extract_bow_treetagger(queries, filename):
    """
    Creates a dictionary out of a TreeTagger-output file (Format: [token]\t[pos]\t[lemma]), 
    where the key is the ID (e.g '45.3'), and the value a set representing the description as a bag-of-words, normalized.
    """
    import re
    results = {}
    
    id_pattern = re.compile('[0-9]{1,3}\.[0-9]{1,3}')
    
    with open(filename, 'r', encoding='utf-8') as f:
        
        for row in f:
            
            row = row.rstrip().split("\t")
            if len(row) == 3:
                
                if re.fullmatch(id_pattern, row[0]) != None:
                    topic = row[0].split('.')[0]
                    results[row[0]] = set()
                    ID = row[0]
                
                elif row[1].startswith('N') and row[0].lower() not in queries.get(ID[:len(topic)], []):
                    if row[2] != "<unknown>":
                        results[ID].add(row[2].lower())
                    elif row[0].isalpha():
                        results[ID].add(row[0].lower())
    
    return results
