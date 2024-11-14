class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        return 

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
