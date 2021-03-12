package io;

import java.io.*;
import java.util.ArrayList;

public class CorpusReader {

	   /**
	     * reads corpus from file. Encapsulates readFile-method.
	     * @param corpusfile corpusfile
	     * @return one line per Entry
	     */
public static ArrayList<String> readCorpus(String corpusfile) {
	File file = new File(corpusfile);
	return readFile(file);
}

	    /**
	     * reads corpus from file.
	     *
	     * @param file corpus file
	     * @return corpus as arraylist
	     */
private static ArrayList<String> readFile(File file) {

	        // store contents
	ArrayList<String> ret = new ArrayList<>();

	try { // IOException, FileNotFoundException

		BufferedReader br = new BufferedReader(new FileReader(file));
	    String line = null;
	    while ((line = br.readLine()) != null) {
	    	ret.add(line);
	    }
	    br.close();
	} catch (IOException e) {
		e.printStackTrace();
	}

	   return ret;
	}
}

