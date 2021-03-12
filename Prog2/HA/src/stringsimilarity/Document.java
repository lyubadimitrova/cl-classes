package stringsimilarity;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;


public class Document {
	
	private String[] documentAsStringArray = new String[]{};

	public Document(String filename) {
	
		Path filePath = Paths.get(filename);     
		List<String> stringList = new ArrayList<String>();
	
		try {
		
			stringList = Files.readAllLines(filePath);
		
		} catch (IOException e) {
			e.printStackTrace();
		}
	
		String[] stringArray = stringList.toArray(new String[]{});
	
		documentAsStringArray = stringArray;     
	}

	public Document(String[] queryDocument) {
	
		documentAsStringArray = queryDocument;
	}

	public String[] getDocumentAsStringArray() {
		return documentAsStringArray;
	}

	public void setDocumentAsStringArray(String[] documentAsStringArray) {
		//unnecessary setter
	}
}
