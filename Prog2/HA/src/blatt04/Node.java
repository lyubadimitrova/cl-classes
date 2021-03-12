package blatt04;

/**
 * @authors: Utaemon Toyota, Lyuba Dimitrova
 * license: MIT Copyright (c) 2017 @authors
 * Written in jdk1.8.0
 */

public class Node {
	
	//Instance variables
	String label;
	
	//Constructor
	Node(String label) {
		this.label = label;
	}
	
	//Methods
	String getLabel() {
		return this.label;
	}
	
	@Override
	public String toString() {
		return this.label;
	}
	
	public static void main(String[] args) {
		
		Node n = new Node("VP");
		System.out.println(n.getLabel());
		
		String nAsString = n.toString();
		System.out.println(nAsString);	
	}
}
