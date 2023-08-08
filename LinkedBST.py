from AbstractCollection import AbstractCollection
from BinaryNode import BinaryNode

class LinkedBST(AbstractCollection):
    """A binary search tree implementation which uses Node objects"""

    def __init__(self):
        self._root = None
        AbstractCollection.__init__(self)
        
    def find(self, item):
        def recurse(node):
            if node is None:
                # Base Case #1: We reached an empty tree or subtree: item is not in the binary search tree
                return None
            elif item == node.data:
                # Base Case #2: Node we are recursing on contains 'item'. Return node.data
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        
        # Constantly returning result of recurse() to the previous recurse()
        return recurse(self._root)
        
    def add(self, item):
        """Adds 'item' to the correct location in this binary search tree"""
        # Inner function so user doesn't have to pass tree._root in add method
        def recurse(node):
            if item < node.data:
                # New item is less than this node's data. Move left!
                if node.left is None:
                    # Base case! Add a new node to the left of this one
                    node.left = BinaryNode(item)
                else:
                    recurse(node.left)
            
            # Item must be greater than or equal to node's data. Move right!
            # Redundant to put else or elif item > node.data
            elif node.right is None:
                # Base case! Add a new node to the right of this one
                node.right = BinaryNode(item)
            else:
                recurse(node.right)
            
        if self.is_empty():
            self._root = BinaryNode(item)
        else:
            recurse(self._root)    
            
        self._numitems += 1
    
    def inorder(self):
        """Prints an inorder traversal of this binary search tree"""
        def recurse(node):
            if node is not None:
                recurse(node.left)
                print(node.data, end=" ")
                recurse(node.right)
        
        recurse(self._root)
    


        