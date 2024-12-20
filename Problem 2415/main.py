from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverse_odd_levels(root):
    if not root:
        return None

    queue = deque([root])
    level = 0

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level % 2 == 1:
            values = [node.val for node in current_level][::-1]
            for i, node in enumerate(current_level):
                node.val = values[i]

        level += 1

    return root

# Example usage:
# Construct the tree [2,3,5,8,13,21,34]
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)

# Reverse odd levels
reversed_root = reverse_odd_levels(root)
