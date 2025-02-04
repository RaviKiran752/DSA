class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

# Usage
bst = BST()
root = None
root = bst.insert(root, 50)
bst.insert(root, 30)
bst.insert(root, 70)
bst.inorder(root)  # Output: 30 50 70
