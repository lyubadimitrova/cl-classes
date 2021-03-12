package blatt04;

/**
 * @authors: Utaemon Toyota, Lyuba Dimitrova
 * license: MIT Copyright (c) 2017 @authors
 * Written in jdk1.8.0
 */

public class NonTerminalNode extends Node {
	
	//Instance variables
	Node[] children;
	
	//Constructor
	NonTerminalNode(String label, Node[] children) {
		super(label);
		this.children = children;
	}
	
	//Instance methods
	Node[] getChildren() {
		return this.children;
	}
	
	@Override
	public String toString() {
		String allChildren = "";
		for(Node child: children) {
			allChildren = allChildren + child.toString() + " ";
		}
		return String.format("%s:( %s)" , super.toString() , allChildren);
	}
	
	/*Aufgabe 3.5
		Die Kindknoten sind als Node[] deklariert, weil ein nicht-terminal Knoten 
		sowohl andere nicht-terminal Knoten als Kinder haben kann, als auch Terminalknoten
	*/
}
