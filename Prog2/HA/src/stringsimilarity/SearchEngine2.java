package stringsimilarity;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class SearchEngine2<E extends Collection<DocumentAsTitle>> {
	
	private E docs;
	private StringSimilarity sim;
	
	public SearchEngine2(E docs, StringSimilarity sim) {
		this.docs = docs;
		this.sim = sim;
	}
	
	DocumentAsTitle findMostSimilarToQuery(DocumentAsTitle query) {
		
		DocumentAsTitle mostSimilar = new DocumentAsTitle(new Document(new String[1]));
		double similarity = 0;
		
		int i = 1;
		
		for(DocumentAsTitle d: docs) {
			
			double currentHighestSimilarity = 0;
			
			if(sim instanceof StringSimilarity)
				currentHighestSimilarity = StringSimilarity.computeSimilarity(d.getDocumentTitle(),query.getDocumentTitle());
			
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
		DocumentAsTitle dat1 = new DocumentAsTitle(d1);
		
		Document d2 = new Document("src/example_data/doc2.txt");
		DocumentAsTitle dat2 = new DocumentAsTitle(d2);
		
		Document d3 = new Document("src/example_data/doc3.txt");
		DocumentAsTitle dat3 = new DocumentAsTitle(d3);
		
		List<DocumentAsTitle> docs = new ArrayList<DocumentAsTitle>();
		docs.add(dat1); 
		docs.add(dat2);
		docs.add(dat3);
		
		SearchEngine2<Collection<DocumentAsTitle>> levSE = new SearchEngine2<Collection<DocumentAsTitle>>(docs,new StringSimilarity());
	
		System.out.println(levSE.findMostSimilarToQuery(new DocumentAsTitle(new Document(new String[]{"another"}))).getDocumentTitle());
		
		System.out.println(levSE.findMostSimilarToQuery(new DocumentAsTitle(new Document(new String[]{"completely"}))).getDocumentTitle());
	}
		
}


