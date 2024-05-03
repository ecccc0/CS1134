from LinkedBinaryTree import *
def create_expression_tree(prefix_exp_str):
    lst = [int(x) if x.isdigit() else x for x in prefix_exp_str.split()]
    def helper(exp, start):
        token=exp[start]
        if isinstance(token, int):
            root = LinkedBinaryTree.Node(token)
            return (root, start+1)
        left = helper(exp, start+1)
        right = helper(exp, left[1])
        root = LinkedBinaryTree.Node(token, left[0], right[0])
        return (root, right[1])
    return LinkedBinaryTree(helper(lst, 0)[0])

def prefix_to_postfix(prefix_exp_str):
    pretree = create_expression_tree(prefix_exp_str)
    res = []
    def helper(root):
        if root is None:
            pass
        else:
            helper(root.left)
            helper(root.right)
            res.append(str(root.data))
    helper(pretree.root)
    return ' '.join(res)