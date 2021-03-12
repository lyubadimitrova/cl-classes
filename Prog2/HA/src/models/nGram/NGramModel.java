package models.nGram;

import data.NGram;


import java.io.*;
import java.util.*;
import java.util.logging.Logger;

public class NGramModel {

    Logger log = Logger.getGlobal();
    private int n;
    private Map<NGram, Integer> counts = new HashMap<>();
    private NGramModel subModel;


    public NGramModel(int n) {
        log.info("Constructing NGramModel:" + n);
        this.n = n;

        this.subModel = new NGramModel(n-1);

    }

    public void train(ArrayList<String[]> corpus) {
        log.info("training NGramModel: " + this.n);
        if (this.subModel != null) {
            this.subModel.train(corpus);
        }

        for (String[] s : corpus) {
            addNGrams(s);
        }
    }

    private void addNGrams(String[] input) {
    	
    	for(int i = 0; i < input.length - this.n - 1; i++) {
    		
    		String[] ng = new String[this.n];
    		
    		Integer oldCount = null;
    		
    		int k = i;
    		
    		for (int j = 0; j < this.n; j++) {
    			ng[j] = input[k];
    			oldCount = counts.get(input[k]);
    			if(oldCount == null) {
    				oldCount = 0;
    			}
    			k++;
    		}
    		NGram ngng = new NGram(ng);
			counts.put(ngng,++oldCount);
    	}
    }


    public void save(String filename) throws IOException {
	// (2c)
	// your implementation
	// here
        filename += this.n;

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filename), "UTF-8"));

        for (Map.Entry<NGram, Integer> entry : this.counts.entrySet()) {
            bw.write(entry.getKey().toString()+"\t"+entry.getValue()+"\n");
        }

        bw.close();


    }

    public void load(String filename) throws IOException {
	
    	BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(filename), "UTF-8"));

        String line = null;
        while ((line = br.readLine()) != null) {
            String[] entry = line.split("\t");
            counts.put(NGram.fromString(entry[0]), Integer.parseInt(entry[1]));
        }
        br.close();    
    }
    
}
