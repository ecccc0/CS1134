from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    res = DoublyLinkedList()
    ptr = lnk_lst.header.next
    while ptr.next is not None:
        # if isinstance(ptr.data, DoublyLinkedList):
        #     res.add_last(copy_linked_list(ptr.data))
        # else:    
        res.add_last(ptr.data)
        ptr = ptr.next
    return res

def deep_copy_linked_list(lnk_lst):
    res = DoublyLinkedList()
    ptr = lnk_lst.header.next
    while ptr.next is not None:
        if isinstance(ptr.data, DoublyLinkedList):
            res.add_last(deep_copy_linked_list(ptr.data))
        else:    
            res.add_last(ptr.data)
        ptr = ptr.next
    return res