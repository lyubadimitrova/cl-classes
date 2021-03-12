package main.java.graphs;

import java.util.Collection;

/**
 * This interface provides methods essential for the work with undirected 
 * graphs with integer nodes. 
 * Any class that implements it can have its own representation of a graph.
 */
public interface Graph {
	
    /** Checks whether an edge between the nodes i and j exists in the graph.
     *  Edges are undirected - order of i and j is irrelevant.
     *
     * @param i node
     * @param j node
     * @return true if an edge between i and j exists in the graph, 
     *     false otherwise
     * @throws InvalidNodeException if i or j are not valid node 
     * identifiers (i.e. &lt; 0) or if i or j are not contained in the graph.
     */
    public boolean containsEdge(int i, int j) throws InvalidNodeException;

    /** Returns all nodes for which there exists an edge that connects
     * them to i.
     * 
     * @param i node to get the neighboring nodes of
     * @return a collection of all nodes for which there exists an edge that 
     * 		   connects them to i
     * @throws InvalidNodeException if i is not a valid node identifier 
     * 		   (i.e. &lt; 0) or if i is not contained in the graph
     */
    public Collection<Integer> getNeighbours(int i) throws InvalidNodeException;
    
    /** Adds an edge between the nodes i and j to the graph.
     *  Edges are undirected - order of i and j is irrelevant.
     *  
     * @param i node 
     * @param j node
     * @return true if an edge between i and j was not present in the graph and
     *        was added, false if an edge between i and j already existed in the graph
     * @throws InvalidNodeException if i or j are not valid node identifiers 
     * 			(i.e. &lt; 0) or if i or j are not contained in the graph
     */
    public boolean addEdge(int i, int j) throws InvalidNodeException;
    
    /** Adds a node i to the graph. 
     * 
     * @param i node to add 
     * @return true if a node i was not present in the graph and
    //         was added, false if it already existed in the graph
     * @throws InvalidNodeException if i is not a valid node identifier 
     *         (i.e. &lt; 0)
     */
    public boolean addNode(int i) throws InvalidNodeException;
}
