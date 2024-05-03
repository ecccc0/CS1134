from LinkedBinaryTree import *
def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise Exception("empty tree")
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return (root.data, root.data)
        elif root.left is None and root.right is not None:
            right = subtree_min_and_max(root.right)
            return (min(right[0], root.data), max(right[1], root.data))
        elif root.left is not None and root.right is None:
            left = subtree_min_and_max(root.left)
            return (min(left[0], root.data), max(left[1], root.data))
        else:
            maxval = root.data
            minval = root.data
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)
            minval = min(minval, left[0], right[0])
            maxval = max(maxval, left[1], right[1])
            return (minval, maxval)
    return subtree_min_and_max(bin_tree.root)