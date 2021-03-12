package main.java.graphs;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

/**
* The class provides a representation
* of an undirected graph with integer nodes in the form of a map. 
* <p>
* Each node is mapped to a list of all its neighbours, e.g.:<br><br>
* 
* 	 0: (1, 2),<br>
*	 1: (0, 2, 3),<br>
*	 2: (0, 1),<br>
*	 3: (1)<br>
* <p>
* The class can create a graph and must implement the methods of the 
*  {@link graphs.Graph} interface. 
* 
* <p>
*
* @author  Lyuba Dimitrova
* @author  Utaemon Toyota
* @version 1.0
* 
*/
public class GraphWithAdjacencyList implements Graph{
	
	private int numberOfNodes;
	private Map<Integer,ArrayList<Integer>> adjacencyList = new HashMap<Integer,ArrayList<Integer>>();
	
	/**
	 * Reads a graph from file and constructs a new GraphWithAdjacencyList.
	 * <p>
	 * @param filename text file in the form<br><br> 4<br>0 1<br>0 2<br>3 1 
	 * <br><br> where the first line is the number of nodes in the graph and
	 * each line after represents an edge							
	 */
	public GraphWithAdjacencyList(String filename) {
		
		try {
			
			List<String> lines = Files.readAllLines(Paths.get(filename));
		
			numberOfNodes = Integer.parseInt(lines.get(0));
			
			String[] nodesInEdge = new String[2]; 
		
			for (int i = 1; i < lines.size(); i++) {
				
				nodesInEdge = lines.get(i).split(" ");
				
				int first = Integer.parseInt(nodesInEdge[0]);
				int second = Integer.parseInt(nodesInEdge[1]);
			
				if(!adjacencyList.containsKey(first)) {
					adjacencyList.put(first, new ArrayList<Integer>());	
					adjacencyList.get(first).add(second);
				} else {
					adjacencyList.get(first).add(second);
				}
				
				if(!adjacencyList.containsKey(second)) {
					adjacencyList.put(second, new ArrayList<Integer>());	
					adjacencyList.get(second).add(first);
				} else {
					adjacencyList.get(second).add(first);
				}
			}	
			
		} catch (IOException e) {
			e.printStackTrace();
		}	
	}

	public boolean containsEdge(int i, int j) throws InvalidNodeException {
		
		//  (worst-case) Laufzeit O(|V|)
		
		if(i >= numberOfNodes || j >= numberOfNodes || i < 0 || j < 0 )  {
			throw new InvalidNodeException("Invalid node!");
		} else {
			if(adjacencyList.get(i).contains(j)) 
				return true;
		}
		return false;
	}

	public Collection<Integer> getNeighbours(int i) throws InvalidNodeException {
		
	//  (worst-case) Laufzeit O(1)
		
		if(i >= numberOfNodes || i < 0)  {
			throw new InvalidNodeException("Invalid node!");
		} else {
				return adjacencyList.get(i);
			}
	}

	public boolean addEdge(int i, int j) throws InvalidNodeException {
		
	//  (worst-case) Laufzeit O(|V|)
		
		if(i >= numberOfNodes || j >= numberOfNodes || i < 0 || j < 0 )  {
			throw new InvalidNodeException("Invalid node!");
		} else {
			if(!adjacencyList.get(i).contains(j)) {
				adjacencyList.get(i).add(j);
				return true;
			}
		}
		return false;
	}

	public boolean addNode(int i) throws InvalidNodeException {
		
		//  (worst-case) Laufzeit O(1)
		
		if(i < 0 || i >= numberOfNodes + 1)  {							//Example: Adding node 10 to set of nodes {0,1,2,3} -> {0,1,2,3,10} no longer has the form {0,...,n}, which messes with the other interface methods
			throw new InvalidNodeException("Invalid node!");
		} else {
			if(i == numberOfNodes) {
				
				numberOfNodes++;
				return true;
			}
		}
		return false;
	}
	
	
}
