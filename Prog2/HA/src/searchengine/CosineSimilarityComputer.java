package searchengine;

import java.util.Map;

public class CosineSimilarityComputer extends SimilarityComputer{
	
	public static double getSimilarity(DocumentAsVector document, DocumentAsVector query) {
		
		double scalarProduct = 0;
		double sumOfSquaredDimensions1 = 0;
		double sumOfSquaredDimensions2 = 0;
			
		Map<String,Integer> doc = document.getTermFrequencyVector();
		Map<String,Integer> q = query.getTermFrequencyVector();
		
		
		if(doc.size() > q.size()) {
			for(String key: doc.keySet()) {
				if(!q.containsKey(key))
					q.put(key, 0);
			}
		} 
		
		if(doc.size() < q.size()) {
			for(String key: q.keySet()) {
				if(!doc.containsKey(key))
					doc.put(key, 0);
			}
		}
		
		for(String key: doc.keySet()) {
			
			scalarProduct += doc.get(key) * q.get(key);
			sumOfSquaredDimensions1 += doc.get(key) * doc.get(key);
			sumOfSquaredDimensions2 += q.get(key) * q.get(key);
		}
		
		return scalarProduct / ( Math.sqrt(sumOfSquaredDimensions1) * Math.sqrt(sumOfSquaredDimensions2) );
	}
}
