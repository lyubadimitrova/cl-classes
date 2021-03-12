package complexnodes;

public class EdgeVariant2 {
	
	private final Node<? extends Number> nodeA;
	private final Node<? extends Number> nodeB;
	private final String label;
	private final double weight;
	    
	public EdgeVariant2(Node<? extends Number> nodeA, Node<? extends Number> nodeB, String label, double weight) {
		this.nodeA = nodeA;
	    this.nodeB = nodeB;
	    this.label = label;
	    this.weight = weight;
	}
	    
    public Node<? extends Number> getFirstNode() {
	    return nodeA;
	}
	    
	public Node<? extends Number> getSecondNode() {
	    return nodeB;
	}    
	    
	public String getLabel() {
	    return label;
	}
	    
	public double getWeight() {
	    return weight;
	}
}
