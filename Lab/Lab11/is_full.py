from LinkedBinaryTree import *
def is_full(root):
    if (root.left is None and not root.right is None) or (root.right is None and not root.left is None):
        return False
    elif root.left is None and root.right is None:
        return True
    return is_full(root.left) and is_full(root.right)