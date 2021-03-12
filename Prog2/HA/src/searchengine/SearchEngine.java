package searchengine;

import java.util.*;

public class SearchEngine<E extends Collection<Document>, F extends SimilarityComputer> {
	
	private E docs;
	private F similarityComputer;
	
	public SearchEngine(E docs, F simComputer) {
		this.docs = docs;
		this.similarityComputer = simComputer;
	}
	
	Document findMostSimilarToQuery(Document query) {
		
		Document mostSimilar = new Document(new String[]{});
		double similarity = 0;
		
		int i = 1;
		
		for(Document d: docs) {
			
			double currentHighestSimilarity = 0;
			
			DocumentAsVector dav = new DocumentAsVector(d);               //without stopwords
			DocumentAsVector qav = new DocumentAsVector(query);
			
			//DocumentAsVector dav = new DocumentAsVector(d, Arrays.asList(new String[]{"he","she", "it", "the", "a", "an", ",", "."}));
			//DocumentAsVector qav = new DocumentAsVector(query,Arrays.asList(new String[]{"he","she", "it", "the", "a", "an", ",", "."}));
			
			if(similarityComputer instanceof CosineSimilarityComputer)
				currentHighestSimilarity = CosineSimilarityComputer.getSimilarity(dav,qav);
			if(similarityComputer instanceof OverlapSimilarityComputer)
				currentHighestSimilarity = OverlapSimilarityComputer.getSimilarity(dav,qav);
			
			System.out.println(String.format("Document %d: ", i) + currentHighestSimilarity);
			
			if(currentHighestSimilarity > similarity) {
				similarity = currentHighestSimilarity;
				mostSimilar = d;
			}
			
			i++;
			
		}
		return mostSimilar;
	}
	
	public static void main(String[] args) {
		
		Document d1 = new Document("src/example_data/doc1.txt");
		Document d2 = new Document("src/example_data/doc2.txt");
		Document d3 = new Document("src/example_data/doc3.txt");
		
		List<Document> docs = new ArrayList<Document>();
		docs.add(d1); 
		docs.add(d2);
		docs.add(d3);
		
		SearchEngine<Collection<Document>,CosineSimilarityComputer> cosineSE = new SearchEngine<Collection<Document>,CosineSimilarityComputer>(docs,new CosineSimilarityComputer());
		SearchEngine<Collection<Document>,OverlapSimilarityComputer> overlapSE = new SearchEngine<Collection<Document>,OverlapSimilarityComputer>(docs,new OverlapSimilarityComputer());
		
		System.out.println(Arrays.toString(cosineSE.findMostSimilarToQuery(new Document("another test".split(" "))).getDocumentAsStringArray()));
		
		System.out.println(Arrays.toString(overlapSE.findMostSimilarToQuery(new Document("another test".split(" "))).getDocumentAsStringArray()));
		
		System.out.println(Arrays.toString(cosineSE.findMostSimilarToQuery(new Document("a test".split(" "))).getDocumentAsStringArray()));
		
		System.out.println(Arrays.toString(overlapSE.findMostSimilarToQuery(new Document("a test".split(" "))).getDocumentAsStringArray()));
		
	}

}
