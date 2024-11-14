class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

# Example Usage
if __name__ == "__main__":
    # Create a binary tree with root value 1
    tree = BinaryTree(1) 
    
    # Insert left and right children
    tree.insert_left(tree.root, 2)
    tree.insert_right(tree.root, 3)
    tree.insert_left(tree.root.left, 4)
    tree.insert_right(tree.root.left, 5)

    # Traversals
    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)  # Output: 4 2 5 1 3
    print("\nPreorder Traversal:")
    tree.preorder_traversal(tree.root)  # Output: 1 2 4 5 3
    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)  # Output: 4 5 2 3 1
