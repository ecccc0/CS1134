from LinkedBinaryTree import *
def bt_even_sum(root):
    if root is None:
        return 0
    left = bt_even_sum(root.left)
    right = bt_even_sum(root.right)
    return root.data + left + right if root.data % 2 == 0 else left + right

