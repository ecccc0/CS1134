def find_min_abs_difference(bst):
    def helper(node):
        if node.left is None and node.right is None:
            return (node.item.key, node.item.key, None)
        else:
            if node.left is None and node.right is not None:
                right = helper(node.right)
                minimum = node.item.key
                maximum = right[1]
                min_diff_tup = (right[0] - node.item.key, right[2])
            elif node.left is not None and node.right is None:
                left = helper(node.left)
                minimum = left[0]
                maximum = node.item.key
                min_diff_tup = (node.item.key - left[1], left[2])
            else:
                left = helper(node.left)
                right = helper(node.right)
                minimum = left[0]
                maximum = right[1]
                min_diff_tup = (node.item.key - left[1], right[0] - node.item.key, left[2], right[2])
            return (minimum, maximum, min(x for x in min_diff_tup if x is not None))
    if bst.root is None:
        raise Exception("empty tree")
    if bst.root.left is None and bst.root.right is None:
        raise Exception("only one node")
    return helper(bst.root)[2]