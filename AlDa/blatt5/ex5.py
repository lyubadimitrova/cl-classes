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
                node.left = self._insert_helper(node.left, key, value)
                return node
            elif key > node.key:
                node.right = self._insert_helper(node.right, key, value)
                return node
            else:
                node.key = key
                node.value = value
                return node
            
        
    def remove(self, key):
        self.root = self._remove_helper(self.root, key)
        self.size -= 1

    def _remove_helper(self, node, key):
        if node is None:
            raise KeyError(key)

        if key == node.key:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            replacement = node.left  # find largest key in left sub-tree
            while replacement.right is not None:
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
        

        
# Traverse
def preOrderTraverse(root):
    if root is not None:
        print ('key', root.key, 'value', root.value)
        preOrderTraverse(root.left)
        preOrderTraverse(root.right)
            
def inOrderTraverse(root):
    if root is not None:
        inOrderTraverse(root.left)
        print ('key', root.key, 'value', root.value)
        inOrderTraverse(root.right)

def postOrderTraverse(root):
    if root is not None:
        postOrderTraverse(root.left)
        postOrderTraverse(root.right)
        print ('key', root.key, 'value', root.value)


a = SearchTree()
#print( a.__len__())
print( a.__len__())
a.insert(6,60)
print( a.__len__())
a.insert(2,20)
print( a.__len__())
a.insert(5,50)
print( a.__len__())
a.insert(3,30)
a.insert(8,80)
print( a.__len__())
a.insert(4,40)
a.insert(6,-10)
a.insert(1,10)
a.insert(7,70)
preOrderTraverse(a.root)
print( a.__len__())
print("\n")
#a.remove(10)
preOrderTraverse(a.root)
print( a.__len__())
print(a)

#print(a.root.value)