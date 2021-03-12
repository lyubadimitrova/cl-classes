package complexnodes;

public class Edge<T> {
	
    private final Node<T> nodeA;
    private final Node<T> nodeB;
    private final String label;
    private final double weight;
    
    public Edge(Node<T> nodeA, Node<T> nodeB, String label, double weight) {
        this.nodeA = nodeA;
        this.nodeB = nodeB;
        this.label = label;
        this.weight = weight;
    }
    
    public Node<T> getFirstNode() {
        return nodeA;
    }
    
    public Node<T> getSecondNode() {
        return nodeB;
    }    
    
    public String getLabel() {
        return label;
    }
    
    public double getWeight() {
        return weight;
    }
}
