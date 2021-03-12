package blatt04;

/**
 * @authors: Utaemon Toyota, Lyuba Dimitrova
 * license: MIT Copyright (c) 2017 @authors
 * Written in jdk1.8.0
 */

public class TerminalNode extends Node {
	
	//Instance variables
	String yield;
	
	//Constructor
	TerminalNode(String label, String yield) {
		super(label);
		this.yield = yield;
	}
	
	//Instance methods
	String getYield() {
		return this.yield;
	}
	
	@Override
	public String toString() {
		return String.format("%s:%s" , super.toString() , this.yield);
	}
}
