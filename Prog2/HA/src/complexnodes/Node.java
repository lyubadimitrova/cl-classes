package complexnodes;

public class Node<T> {
    private final String label;
    private final T value;
    
    Node(String label, T value) {
        this.label = label;
        this.value = value;
    }
    
    public String getLabel() {
        return label;
    }
    
    public T getValue() {
        return value;
    }
}
