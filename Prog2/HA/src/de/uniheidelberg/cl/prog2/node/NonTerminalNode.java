package de.uniheidelberg.cl.prog2.node;

import java.util.*;
import java.util.regex.*;



public class NonTerminalNode extends Node {

	static final char OPENPAREN = '(';
	static  final char CLOSINGPAREN = ')';

	private ArrayList<Node> children;

	public NonTerminalNode( String label, ArrayList<Node> children ) {
		super( label );
		this.children = children;
	}

	ArrayList<Node> getChildren() {
		return this.children;
	}

	public String toString() {

		String result = getLabel()+":( ";
		for ( Node c: this.children ) {
			result += c.toString() + " ";
		}
		result += ")";
		return result;
	}


	public static Node parse( StringBuilder nodeRepr ) {

		// Subtask (1) 1 Punkt
		// * compile a suitable pattern that recognizes the start of a non-terminal
		//   node
		// * compile a second pattern that recognizes the end of a non-terminal
		//   node
		// * apply both patterns to nodeRepr and return two instances of the Matcher
		//   class called 'opening' and 'closing' respectively
		//

		Matcher opening = Pattern.compile( "^\\s*([A-Z]+)\\s*:\\(" ).matcher( nodeRepr );
		Matcher closing = Pattern.compile( "\\s*(\\))\\s*$" ).matcher( nodeRepr );

		Pattern emptypattern = Pattern.compile("^\\s*$");

		// Subtask (2) 0.5 Punkte
		// write an if test that uses your regular expressions
		// to test if you have a non-terminal
		

		 if (opening.find() && closing.find()){

			NonTerminalNode nt = new NonTerminalNode(opening.group(1), new ArrayList<Node>());
			

			// we remove the parentheses that enclosed the non-terminal node
			// we are then going to check inside the non-terminal node string
			// to see if it contains further non-terminal or terminal nodes

			// we delete the closing parentheses at the end first so that indices for 
			// the start don't move!
			nodeRepr.delete(closing.end()-1,closing.end());
			nodeRepr.delete(0, opening.end());
			
			
			while (nodeRepr.length()>0){
				

				// Subtask (3) 0.5 Punkte
				// * compile a pattern that matches on a terminal node
				// * apply its matcher method to nodeRepr and assign the resulting
				//   Matcher object to a variable 'term'

				// <your implementation here>
				Matcher term = Pattern.compile( "\\s*([A-Z]+):([A-Za-z]+)" ).matcher( nodeRepr );

				// we check if we have terminal in front of us
				if (term.lookingAt()){

					// Subtask (4) 0.5 Punkte
					// * extract the substring that represents the terminal
					// * assign it to a String variable

					// NB: If you  used the right kind of capturing group in your regular
					// expression above, you could now access the relevant string with
					// the group-method of your Matcher term.

					// <your implementation here>
					String t = term.group(1)+ ":" +term.group(2);

					// Subtask (5) 0.5 Punkte
					// now that you have isolated the string that
					// represents the terminal, 
					// * construct a new terminal node by using the static 
					//   parse-method of the TerminalNode class (you pass the 
					//   string you extracted above to the parse-method)
					// * assign the new Node instance to a variable called 'tnode'

					// <your implementation here>;
					Node tnode = TerminalNode.parse(new StringBuilder(t));

					// we add the Node tnode that we just generated
					// to the list of children of the  current non-terminal node nt
					nt.getChildren().add(tnode);
					

					// shorten nodeRepr: we throw away the substring that represents
					// the terminal we just built a node for
					nodeRepr.delete(0,term.end());
					//continue the while loop!
					continue;
					
				}else {
					// potentially, we can now find a non-terminal

					// Subtask (6) 0.5 Punkte
					// use the Pattern 'emptypattern' (see above) in an if-test
					// to check if nodeRepr contains no further material that could be
					// a node; if that is so, break out of the while loop

					if (emptypattern.matcher(nodeRepr).matches()){
						break;
					}

					// because the  non-terminal node that we have in the string  now
					// could be followed by another terminal or non-terminal
					// we have to determine where the upcoming non-terminal ends

					// idea: we go from the beginning of the sequence to the right
					// until we hit a closing parenthesis AND we have seen as many
					// closing parentheses as opening parentheses
					// we store  the index of the last closing parenthesis that is
					// part of the non-terminal
					//
					char c;
					int openings = 0; // count var for opening parentheses we've seen
					int closings = 0; // count var for closing parentheses we've seen


					// Subtask (7) 1 Punkt
					//
					// implement the while loop that iterates over the sequence
					// until you have seen an equal number of closing and opening
					// parentheses; at that point break out of the loop
					//

					int i = 0;
					while (i < nodeRepr.length() ) {
						
						c = nodeRepr.charAt(i);
						
						if (openings==closings&&openings!=0){
							break;
						}
						if (c == OPENPAREN){
							openings++;
						}
						if (c == CLOSINGPAREN){
							closings++;
						}

						i++;
					}

					// now we extract the string that represents the non-terminal
					// using the substring method

					// NB: make sure you keep the final parenthesis as part of the
					// sequence you give to the new StringBuilder
					StringBuilder newnonterm = new StringBuilder ( nodeRepr.substring(0,i) );

					// Subtask (8) 0.5 Punkte

					// * now you use recursion to send the sequence we just found
					//   and  stored in the above StringBuilder instance
					//   to the static parse-Method of the  NonTerminalNode class for parsing
					// * assign the Node that you get back to a variable
					//   of type Node called 'ntnode'


					Node ntnode = Node.parse(newnonterm);

					// add Node to children of current non-terminal node nt
					nt.getChildren().add(ntnode);

					//shorten nodeRepr
					nodeRepr.delete(0,i);
					//continue the while loop!
					continue;
				}
			}
			return nt;

		}else{
			// it's not a non-terminal node after all
			return null;
		}
	}
}

