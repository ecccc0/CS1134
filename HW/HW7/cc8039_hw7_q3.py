from LinkedBinaryTree import *
def is_height_balanced(bin_tree):
    def helper(root):
        if root is None:
            return (True, 0)
        left = helper(root.left)
        right = helper(root.right)
        height = max(left[1], right[1] + 1)
        if not (left[0] and right[0]) or abs(left[1] - right[1]) > 1:
            return (False, height)
        return (True, height)
    if bin_tree.is_empty():
        raise Exception("empty tree")
    return helper(bin_tree.root)[0]