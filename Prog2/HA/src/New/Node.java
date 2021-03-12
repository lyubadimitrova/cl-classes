package de.uniheidelberg.cl.prog2.node;

/**
* We want to be able to parse input of the following types into Node etc objects:
* 
* S:( NE:Hans VP:( VVFIN:liebt NE:Maria ) )
* NE:Hans
* NE
* S:(NP:( ART:The ADJA:quick ADJA:brown NN:fox ) VP:( VVFIN:jumps PP:( APPR:over NP:( ART:the ADJA:lazy NN:dog ) ) ) )
*/

import java.util.*;
import java.util.regex.*;

public class Node {

	private String label;

	public Node( String label ) {
		this.label = label;
	}

	public String getLabel() {
		return this.label;
	}

	public String toString() {
		return this.label;
	}

	public static Node parse( StringBuilder nodeRepr ) {

	    // see if the node is a terminal
		Node n = TerminalNode.parse( nodeRepr );
		
		// if it's not a terminal, try to treat it as a non-terminal
		if ( n == null ) {
			n = NonTerminalNode.parse( nodeRepr );
		}

		// if that doesn't work either
		if ( n == null ) {

			Matcher m = Pattern.compile( "^\\s*([^\\s:()]+)\\s*$" ).matcher( nodeRepr );
	    	// lookingAt() returns true if, and only if, a prefix of the input sequence matches this matcher's pattern
			if ( m.lookingAt() ){
				n = new Node( m.group(1) );
				// we delete the complete matched region
				// m.end() returns the offset after the last character matched.
				nodeRepr.delete(0, m.end());
			}else{
				System.out.println("no match off |"+nodeRepr+"|");
			}
		}
		return n;
	}

	public static void main( String[] args ) {
    	// These are some test trees similar to what's in the parse-trees.txt file.
		String s1 =  "S:( NE:Hans VP:( VVFIN:liebt NE:Maria ) )";
		String s2  = "S:( NP:( ART:The ADJA:quick ADJA:brown NN:fox ) VP:( RP:slowly VVFIN:jumps PP:( APPR:over NP:( ART:the ADJA:lazy NN:dog ) ) ) )";
		String s2b  = "S:(NE:Hans VP:( RP:slowly VVFIN:jumps PP:( APPR:over NP:( ART:the ADJA:lazy NN:dog ) ) ) )";
		String s3 = " NE:Hans VP:(VVFIN:liebt) ";
		String s4 = " VP:( VVFIN:liebt NE:Maria ) ";
		String t1 = "NE:Hans";
		String t2 = "NE";
		// choose input
		String input = t2;
		// NB: we remove white space
		StringBuilder sb = new StringBuilder( input.trim());

		System.err.println("parsed node: " + Node.parse( sb ) );

	}

}
