package searchengine;

import java.util.*;

public class DocumentAsVector {
	
	private Map<String,Integer> termFrequencyVector= new HashMap<String,Integer>();

	public DocumentAsVector(Document doc) {
		
		String[] documentLines = doc.getDocumentAsStringArray();
		for(int i = 0; i < documentLines.length; i++) {              
			countTerm(documentLines[i]);
		}
	}
	
	public DocumentAsVector(Document doc, List<String> stopwordsList) {
		
		String[] documentLines = doc.getDocumentAsStringArray();
		
		for(int i = 0; i < documentLines.length; i++) {
			
			if(!stopwordsList.contains(documentLines[i].toLowerCase())) {   //delete .toLowerCase() to get case-sensitive vector
				countTerm(documentLines[i]);
			}
			
		}
	}
	
	private void countTerm(String documentLine) {
		
		documentLine = documentLine.toLowerCase();			//delete this line to get case-sensitive vector
		
		int currentTermFrequency = 1;

		if(!termFrequencyVector.containsKey(documentLine)) {
			termFrequencyVector.put(documentLine, currentTermFrequency);
		} else {
			termFrequencyVector.put(documentLine, ++currentTermFrequency);
		}
	}
	
	public Map<String,Integer> getTermFrequencyVector() {
		return termFrequencyVector;
	}

	public void setTermFrequencyVector(Map<String,Integer> termFrequencyVector) {
		//setter unnecessary for the implementation
	}
	
	public void printTermFrequencyVector() {
		
		Iterator<String> iterator = termFrequencyVector.keySet().iterator();

		while (iterator.hasNext()) {
		   String key = iterator.next().toString();
		   Integer value = termFrequencyVector.get(key);

		   System.out.println(String.format("%-10s %10s", key, value));
		}
	}
	
	public static void main(String[] args) {
		
		Document doc = new Document("src/example_data/doc3.txt");
		
		//DocumentAsVector vector = new DocumentAsVector(doc);
		//vector.printTermFrequencyVector();
		
		List<String> stopwords = new ArrayList<String>();
		stopwords.addAll(Arrays.asList(new String[]{"he","she", "it", "the", "a", "an", ",", "."}));
		
		DocumentAsVector vectorNoStopWords = new DocumentAsVector(doc, stopwords);
		//vectorNoStopWords.printTermFrequencyVector();
		
		Document query = new Document("can a swallow carry a coconut".split(" "));
		DocumentAsVector queryVector = new DocumentAsVector(query);
		
		double sim = CosineSimilarityComputer.getSimilarity(vectorNoStopWords,queryVector);    //not ~0.408 because vectors are not case-sensitive
		System.out.println(sim);
		
		System.out.println(OverlapSimilarityComputer.getSimilarity(queryVector,vectorNoStopWords));
		
		
	}
	
}
