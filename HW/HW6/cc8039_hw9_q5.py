from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(node1, node2):
        if node1.data is None and node2.data is not None:
            res = DoublyLinkedList()
            while node2.data is not None:
                res.add_last(node2.data)
                node2 = node2.next
        elif node1.data is not None and node2.data is None:
            res = DoublyLinkedList()
            while node1.data is not None:
                res.add_last(node1.data)
                node1 = node1.next

        else:
            if node1.data > node2.data:
                res = merge_sublists(node1, node2.next)
                res.add_first(node2.data)
            else:
                res = merge_sublists(node1.next, node2)
                res.add_first(node1.data)
        return res
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)