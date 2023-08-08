class BinaryNode:
    """A node for use in any binary tree"""

    def __init__(self, data, left=None, right=None):
        self._left = left
        self._right = right
        self._data = data
        
    def __str__(self):
        return str(self.data)
        
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, item):
        self._left = item
    
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, item):
        self._right = item
    
    @property
    def data(self):
        return self._data