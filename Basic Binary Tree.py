class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Simple traversal to print the tree
def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.value, end=" ")
        print_tree(node.right)

# Test the print function
print("In-order Traversal of the tree:")
print_tree(root)
