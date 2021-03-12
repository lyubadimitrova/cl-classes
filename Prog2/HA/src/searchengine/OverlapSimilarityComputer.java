package searchengine;

import java.util.*;

public class OverlapSimilarityComputer extends SimilarityComputer{
	
	public static double getSimilarity(DocumentAsVector document, DocumentAsVector query) {
		
		Map<String,Integer> doc = document.getTermFrequencyVector();
		Map<String,Integer> q = query.getTermFrequencyVector();
		
		for(String word: q.keySet()) {
			if(doc.keySet().contains(word))
				return 1;
		}
		
		return 0;
	}
}
