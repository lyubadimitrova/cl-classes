package main.java.graphs;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

/**
* The class provides a representation of an undirected graph with integer
* nodes in the form of a matrix. <p> The graph is represented
* by a two-dimensional matrix with n rows and n columns, where n is
* the number of nodes in the graph. Every field [i][j] in the matrix 
* represents an edge and has the value 1 if an edge between i and j 
* exists, 0 otherwise.
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
public class GraphWithAdjacencyMatrix implements Graph {
	
	private int numberOfNodes;
	private int adjacencyMatrix[][];
	
	/**
	 * Reads a graph from file and constructs a new GraphWithAdjacencyMatrix.
	 * <p>
	 * @param filename text file in the form<br><br> 4<br>0 1<br>0 2<br>3 1 
	 * <br><br> where the first line is the number of nodes in the graph and
	 * each line after represents an edge							
	 */
	public GraphWithAdjacencyMatrix(String filename) {
		
		try {
			
			List<String> lines = Files.readAllLines(Paths.get(filename));
		
			numberOfNodes = Integer.parseInt(lines.get(0));

			String[] first_line = lines.get(0).split(" ")

			Map<String, Integer> myMap = new HashMap<String, Integer>();
			for(int i = 0; i < first_line.length; i++) {
				myMap.put(first_line[i], i)
			}
			adjacencyMatrix = new int[numberOfNodes][numberOfNodes];
			
			String[] nodesInEdge;
			
			for(int i = 1; i < lines.size(); i++) {
				nodesInEdge = lines.get(i).split(" ");
				adjacencyMatrix[myMap.get(nodesInEdge[0])][yMap.get(nodesInEdge[1])] = 1;
			}	
		} catch (IOException e) {
			e.printStackTrace();
		}	
	}

	@Override
	public boolean containsEdge(int i, int j) throws InvalidNodeException {
		
		//  (worst-case) Laufzeit O(1)
		
		if(i >= numberOfNodes || j >= numberOfNodes || i < 0 || j < 0 )  {
			throw new InvalidNodeException("Invalid node!");
		} else {
			if(adjacencyMatrix[i][j] == 1)
				return true;
		}
		return false;
	}

	@Override
	public Collection<Integer> getNeighbours(int i) throws InvalidNodeException {
		
		//  (worst-case) Laufzeit O(|V|)
		
		if(i >= numberOfNodes || i < 0)  {
			throw new InvalidNodeException("Invalid node!");
		} else {
			Collection<Integer> neighbours = new ArrayList<Integer>();
			for(int j = 0; j < numberOfNodes ; j++) {
				if(adjacencyMatrix[i][j] == 1)
					neighbours.add(j);
			}
			return neighbours;
		}
	}

	@Override
	public boolean addEdge(int i, int j) throws InvalidNodeException {
		
		//  (worst-case) Laufzeit O(1)
		
		if(i >= numberOfNodes || j >= numberOfNodes || i < 0 || j < 0 )  {
			throw new InvalidNodeException("Invalid node!");
		} else {
			if(adjacencyMatrix[i][j] == 0) {
				adjacencyMatrix[i][j] = 1;
				return true;	
			}
		}
		return false;
	}

	@Override
	public boolean addNode(int i) throws InvalidNodeException {
		
		//  (worst-case) Laufzeit O(1)
		
		if(i < 0 || i >= numberOfNodes + 1)  {							//Example: Adding node 10 to set of nodes {0,1,2,3} -> {0,1,2,3,10} no longer has the form {0,...,n}, which messes with the other interface methods
			throw new InvalidNodeException("Invalid node!");
		} else {
			if(i == numberOfNodes) {
				
				numberOfNodes++;
				
				int newAdjacencyMatrix[][] = new int[numberOfNodes][numberOfNodes];
				
				for(int j = 0; j < adjacencyMatrix.length - 1; j++)
					  for(int k = 0; k < adjacencyMatrix.length; k++)
						  newAdjacencyMatrix[j][k] = adjacencyMatrix[j][k];
				
				adjacencyMatrix = newAdjacencyMatrix;
						
				return true;
				
			}
		}
		return false;	
	}
}
