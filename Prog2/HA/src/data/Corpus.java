package data;

import io.CorpusReader; // (1b)
import java.io.*;
import java.nio.file.*;	// (1b)
import java.nio.charset.*;
import java.util.ArrayList;

public class Corpus {

    /* An ArrayList of String-Arrays. Each String-Array is a tokenized sentence*/
    private ArrayList<String[]> content;

    private Corpus(ArrayList<String[]> content){
        this.content = content;
    }

    public Corpus(String filename) throws IOException {
        this.load(filename);
    }

    public static Corpus readCorpusFromFile(String filename) {
        // we get a list of sentence strings from a method
	// of the CorpusReader class.
        ArrayList<String> content = CorpusReader.readCorpus(filename);
        ArrayList<String[]> corp = new ArrayList<String[]>();
        for(String str:content) {
        	String[] tokens = str.split(" ");
        	String[] sent = new String[tokens.length];
        	for(int i = 0; i < tokens.length-1; i++) {
        		sent[i] = tokens[i];
        	}
        	corp.add(sent);
        }
        Corpus corpus = new Corpus(corp);
        return corpus;
    }
 
    /* load a  stored corpus. each line is a sentence. the words in each
    sentence are tab-separated (see split)*/
    private void load(String filename) throws IOException {
    	Path file = Paths.get(filename);
    	Charset charset = Charset.defaultCharset();
        try {
        	
        	BufferedReader br = Files.newBufferedReader(file,charset);
        	this.content = new ArrayList<>();

        	String line = null;
        	while ((line = br.readLine()) != null) {
        		this.content.add(line.split("\t"));
        	}
        	br.close();
        } catch (IOException x) {
        	System.err.format( "IOException: %s%n" , x ); }
    }

    /*when writing, separate each word in a sentence array by tabs*/
    public void save(String filename) throws IOException {
    	try {
    		
    		Path file = Paths.get(filename);
        	Charset charset = Charset.defaultCharset();
        	BufferedWriter bw = Files.newBufferedWriter(file,charset);

        	for (String[] s : this.content) {
        		bw.write(String.join("\t", s)+"\n");
        	}

        	bw.close();
    	} catch (IOException x) {
        	System.err.format( "IOException: %s%n" , x ); }
    }

    public ArrayList<String[]> getCorpus() {
        return this.content;
    }
    public static void main() {
    	
    }
}
