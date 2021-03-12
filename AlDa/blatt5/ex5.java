class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class SearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, key, value):
        self.root = self._insert_helper(self.root, key, value)

    def _insert_helper(self, node, key, value):
        if node is None:
            self.size += 1
            return Node(key, value)
        else:
            if key < node.key:
                node.left = insert_helper(node.left, key, value)
                self.size += 1
                return node
            elif key > node.key:
                node.right = _insert_helper(node.right, key, value)
                self.size += 1
                return node
            else:
                node.key = key
                node.value = value
                return node

def remove(self, key):
    self.root = self._remove_helper(self.root, key)

def _remove_helper(node, key):
    if node is None:
        raise KeyError(key)

    if key == n.key:
        if node.left is None and node.right is None:
            return None
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        replacement = node.left
        while node.left is not None:
            replacement = replacement.right

        node.key = replacement.key
        node.value = replacement.value
        node.left = self._remove_helper(node.left, replacement.key)
        return node

    elif key < node.key:
        node.left = self._remove_helper(node.left, key)
        return node
    elif key > node.key:
        node.right = self._remove_helper(node.right, key)
        return node


K smallVal = smallest(n.getRight());
n.setKey(smallVal);
n.setRight( delete(n.getRight(), smallVal) );
return n; 

if (key.equals(n.getKey())) {
        // n is the node to be removed
        if (n.getLeft() == null && n.getRight() == null) {
            return null;
        }
        if (n.getLeft() == null) {
            return n.getRight();
        }
        if (n.getRight() == null) {
            return n.getLeft();
        }
       
        // if we get here, then n has 2 children
        // code still needs to be added here...
    }

public void delete(K key) {
    root = delete(root, key);
}
 
private BSTnode<K> delete(BSTnode<K> n, K key) {
    if (n == null) {
        return null;
    }
    
    if (key.equals(n.getKey())) {
       // n is the node to be removed
       // code must be added here
    }
    
    else if (key.compareTo(n.getKey()) < 0) {
        n.setLeft( delete(n.getLeft(), key) );
        return n;
    }
    
    else {
        n.setRight( delete(n.getRight(), key) );
        return n;
    }
}
private BSTnode<K> insert(BSTnode<K> n, K key) throws DuplicateException {
    if (n == null) {
        return new BSTnode<K>(key, null, null);
    }
     
    if (n.getKey().equals(key)) {
        throw new DuplicateException();
    }
    
    if (key.compareTo(n.getKey()) < 0) {
        // add key to the left subtree
        n.setLeft( insert(n.getLeft(), key) );
        return n;
    }
    
    else {
        // add key to the right subtree
        n.setRight( insert(n.getRight(), key) );
        return n;
    }
}

public void insert(K key) throws DuplicateException {
    root = insert(root, key);
}

public void setLeft(BSTnode<K> newL) { left = newL; }
public void setRight(BSTnode<K> newR) { right = newR; }

public class BST<K extends Comparable<K>, V> {
    // *** fields ***
    private BSTnode<K, V> root; // ptr to the root of the BST
 
    // *** constructor ***
    public BST() { root = null; } 
    
    // *** methods ***  
    
    public void insert(K key, V value) throws DuplicateException {...}
      // add key and associated value to this BST;
      // error if key is already there
      
    public void delete(K key) {...}
      // remove the node containing key from this BST if it is there;
      // otherwise, do nothing
      
    public V lookup(K key) {...}
      // if key is in this BST, return its associated value; otherwise, return null
     
    public void print(PrintStream p) {...}
      // print the values in this BST in sorted order (to p)



def insert(self, key, value):
        
        if self.root:
            parent = None
            x = self.root
            while x is not None:
                parent = x
                if key < x.key:
                    x = x.left
                elif key > x.key:
                    x = x.right
                else:
                    x.value = value
                    break
            
            if key < parent.key:
                parent.left = Node(key, value)
                self.size += 1
            elif key > parent.key:
                parent.right = Node(key, value)
                self.size += 1   

        else:
            self.root = Node(key, value)
            self.size += 1
            
        
    def remove(self, key):
        
        node = self.find(key)
        if node:
            if node.left is None and node.right is None:
                parent = self._parent(key)
                parent.left = None
                parent.right = None
            elif node.right is None: 
                parent = self._parent(key)
                if parent.right == node:
                    parent.right = node.left
                else:
                    parent.left = node.left
            elif node.left is None: 
                parent = self._parent(key)
                if parent.right == node:
                    parent.right = node.right
                else:
                    parent.left = node.right
            else:
                changed = False
                new_node = node.left
                while new_node.right:
                    print(new_node.key, new_node.right.key)
                    new_node = new_node.right
                    changed = True
                if changed:
                    parent = self._parent(new_node.key)
                    parent.right = new_node.left
                    new_node.right = node.right
                    new_node.left = node.left
                    if node.key == self.root.key:
                        self.root = new_node
                    else:
                        parent_of_node = self._parent(node.key)
                        if parent_of_node.left == node:
                            parent_of_node.left = new_node
                        else:
                            parent_of_node.right = new_node
                else:
                    parent = self._parent(node.key)
                    parent.left = new_node
                    new_node.right = node.right
                
            self.size -= 1      
            
        else:
            raise KeyError(key)
        
        
    def find(self, key):
        x = self.root
        while x:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
        
        return None
    
    
    def _parent(self, key):
        x = self.root
        while x:
            if (x.left and x.left.key == key) or (x.right and x.right.key == key): 
                return x
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
        