package de.uniheidelberg.cl.prog2.node;

import java.util.*;
import java.util.regex.*;

public class TerminalNode extends Node {

    private String yield;

    public TerminalNode( String label, String yield ) {
	super( label );
	this.yield = yield;
    }

    public String getYield() {
	return this.yield;
    }

    public String toString() {
	return getLabel()+":"+this.yield;
    }

    public static Node parse( StringBuilder nodeRepr ) {

	Matcher m = Pattern.compile( "\\s*([^\\s:()]+):([^\\s:()]+)\\s*" ).matcher( nodeRepr );
	TerminalNode t = null;
	if ( m.matches() ){
	    t = new TerminalNode( m.group( 1 ), m.group( 2 ) );
	    nodeRepr.delete(0, m.end());
	}
	
	return t;
    }

}
