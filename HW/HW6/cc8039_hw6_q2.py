from DoublyLinkedList import *

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for x in num_str:
            self.data.add_last(int(x))
        while len(self.data) > 1 and self.data.header.next.data == 0:
            self.data.delete_first()
    
    def __add__(self, other):
        res = Integer("")
        carry = 0
        ptr1 = self.data.trailer.prev
        ptr2 = other.data.trailer.prev
        while ptr1.data is not None and ptr2.data is not None:
            cur_res = ptr1.data + ptr2.data + carry
            res.data.add_first(cur_res % 10)
            carry = cur_res // 10
            ptr1 = ptr1.prev
            ptr2 = ptr2.prev
        longer = None
        if ptr1.data is not None:
            longer = ptr1
        else:
            longer = ptr2
        while longer is not None and longer.data is not None:
            res.data.add_first((longer.data + carry) % 10)
            carry = (longer.data + carry) // 10
            longer = longer.prev
        if carry != 0:
            res.data.add_first(carry)
        return res
    
    def __repr__(self):
        ptr = self.data.header.next
        num_str = ""
        while ptr.data is not None:
            num_str += str(ptr.data)
            ptr = ptr.next
        return num_str 

    

        