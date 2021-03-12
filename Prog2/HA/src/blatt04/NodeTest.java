package blatt04;

/**
 * @authors: Utaemon Toyota, Lyuba Dimitrova
 * license: MIT Copyright (c) 2017 @authors
 * Written in jdk1.8.0
 */

public class NodeTest {

	public static void main(String[] args) {
		
		TerminalNode t1 = new TerminalNode("ART", "The");
		TerminalNode t2 = new TerminalNode("ADJA", "quick");
		TerminalNode t3 = new TerminalNode("ADJA", "brown");
		TerminalNode t4 = new TerminalNode("NN", "fox");
		TerminalNode t5 = new TerminalNode("VVFIN", "jumps");
		TerminalNode t6 = new TerminalNode("APPR", "over");
		TerminalNode t7 = new TerminalNode("ART", "the");
		TerminalNode t8 = new TerminalNode("ADJA", "lazy");
		TerminalNode t9 = new TerminalNode("NN", "dog");
		
		TerminalNode[] NP1 = new TerminalNode[]{t1, t2, t3, t4};
		NonTerminalNode nt1 = new NonTerminalNode("NP", NP1);
		
		TerminalNode[] NP2 = new TerminalNode[]{t7, t8, t9};
		NonTerminalNode nt2 = new NonTerminalNode("NP", NP2);
		
		Node[] PP = new Node[]{t6, nt2};
		NonTerminalNode nt3 = new NonTerminalNode("PP", PP);
		
		Node[] VP = new Node[]{t5, nt3};
		NonTerminalNode nt4 = new NonTerminalNode("VP", VP);
		
		NonTerminalNode[] S = new NonTerminalNode[]{nt1, nt4};
		NonTerminalNode nt5 = new NonTerminalNode("S", S);
		
		System.out.println(nt5.toString());
	}
}
