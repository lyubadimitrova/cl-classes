package blatt03;

import java.util.Arrays; 

public class Sentence {
	
	String[] tokens;
	
	Sentence (String [] array) {
		this.tokens = array;
	}
	
	String[] getSentence () {
		return this.tokens;
	}
	
	
	public static void main(String[] args) {
		String[] arr  = new String[]{"I", "love", "Java", "."};
		Sentence sent = new Sentence(arr);
		System.out.println(Arrays.toString(sent.getSentence()));

	}

}
