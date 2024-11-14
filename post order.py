def postorder_traversal(self, node):
    if node:
        self.postorder_traversal(node.left)  
        self.postorder_traversal(node.right) 
        print(node.data, end=" ")