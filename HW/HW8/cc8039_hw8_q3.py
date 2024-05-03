from BinarySearchTreeMap import *
def restore_bst(prefix_lst):
    def helper(prefix_lst, start_pos, val):
        new_item = BinarySearchTreeMap.Item(prefix_lst[start_pos])
        cur_node = BinarySearchTreeMap.Node(new_item)
        if start_pos == 0:
            return cur_node, cur_node
        connect_pos = None
        while prefix_lst[start_pos] < prefix_lst[start_pos - 1]:
            start_pos -= 1
            prev_node = cur_node
            new_item = BinarySearchTreeMap.Item(prefix_lst[start_pos])
            cur_node = BinarySearchTreeMap.Node(new_item)
            if val is not None and cur_node.item.key > val and connect_pos is None:
                connect_pos = prev_node
            cur_node.left = prev_node
            prev_node.parent = cur_node
            if start_pos == 0:
                if connect_pos is None: 
                    return cur_node, cur_node
                return connect_pos, cur_node
        prev_connect_pos, curr_root = helper(prefix_lst, start_pos - 1, cur_node.item.key)
        prev_connect_pos.right = cur_node
        cur_node.parent = prev_connect_pos
        if connect_pos is None:
            connect_pos = cur_node
        if val is not None and val > curr_root.item.key > connect_pos.item.key:
            return curr_root, curr_root
        return connect_pos, curr_root
    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst.root = helper(prefix_lst, len(prefix_lst) - 1, None)[1]
    bst.n = len(prefix_lst)
    return bst