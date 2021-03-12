package stringsimilarity;

public class DocumentAsTitle {
	
	private String documentTitle = new String();

	public DocumentAsTitle(Document doc) {
		
		documentTitle = doc.getDocumentAsStringArray()[0];
	}
	
	public String getDocumentTitle() {
		return documentTitle;
	}

	public void setDocumentTitle(String documentTitle) {
		//setter unnecessary for the implementation
	}
	
public static void main(String[] args) {
		
		Document d1 = new Document("src/example_data/doc1.txt");
		DocumentAsTitle dat1 = new DocumentAsTitle(d1);
		
		Document d2 = new Document("src/example_data/doc2.txt");
		DocumentAsTitle dat2 = new DocumentAsTitle(d2);
		
		Document d3 = new Document("src/example_data/doc2.txt");
		DocumentAsTitle dat3 = new DocumentAsTitle(d3);
		
		double sim = StringSimilarity.computeSimilarity(dat2.getDocumentTitle(), dat3.getDocumentTitle());
		System.out.println(sim);
		
		double sim2 = StringSimilarity.computeSimilarity(dat1.getDocumentTitle(), dat2.getDocumentTitle());
		System.out.println(sim2);
	}
}
