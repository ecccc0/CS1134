from DoublyLinkedList import *
class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        cnt = 1
        for i in range(1, len(orig_str)):
            if orig_str[i] == orig_str[i - 1]:
                cnt += 1
            else:
                self.data.add_last((orig_str[i - 1], cnt))
                cnt = 1
        if len(orig_str) != 0:
            self.data.add_last((orig_str[len(orig_str) - 1], cnt))

    def __add__(self, other):
        res = CompactString("")
        ptr = self.data.header.next
        while ptr.next.data is not None:
            res.data.add_last(ptr.data)
            ptr = ptr.next
        if ptr.data[0] == other.data.header.next.data[0]:
            res.data.add_last((ptr.data[0], ptr.data[1] + other.data.header.next.data[1]))
            ptr = other.data.header.next.next
        else:
            res.data.add_last(ptr.data)
            ptr = other.data.header.next
        while ptr.data is not None:
            res.data.add_last(ptr.data)
            ptr = ptr.next
        return res

    def __lt__(self, other):
        ptr1 = self.data.header.next
        ptr2 = other.data.header.next
        while ptr1.data == ptr2.data and ptr1.data is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr1.data is None and ptr2.data is None:
            return False
        elif ptr1.data is None and ptr2.data is not None:
            return True
        elif ptr1.data is not None and ptr2.data is None:
            return False
        else:
            if ptr1.data[0] == ptr2.data[0]:
                if ptr1.data[1] > ptr2.data[1]:
                    if ptr2.next.data is None:
                        return False
                    return ptr1.data[0] < ptr2.next.data[0]
                else:
                    if ptr1.next.data is None:
                        return True
                    return ptr1.next.data[0] < ptr2.data[0]
            return ptr1.data[0] < ptr2.data[0]

    def __le__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        while cursor1.data == cursor2.data and cursor1.data is not None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1.data is None and cursor2.data is None:
            return True
        elif cursor1.data is None and cursor2.data is not None:
            return True
        elif cursor1.data is not None and cursor2.data is None:
            return False
        else:
            if cursor1.data[0] == cursor2.data[0]:
                if cursor1.data[1] > cursor2.data[1]:
                    if cursor2.next.data is None:
                        return False
                    return cursor1.data[0] < cursor2.next.data[0]
                else:
                    if cursor1.next.data is None:
                        return True
                    return cursor1.next.data[0] < cursor2.data[0]
            return cursor1.data[0] < cursor2.data[0]

    def __gt__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        while cursor1.data == cursor2.data and cursor1.data is not None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1.data is None and cursor2.data is None:
            return False
        elif cursor1.data is None and cursor2.data is not None:
            return False
        elif cursor1.data is not None and cursor2.data is None:
            return True
        else:
            if cursor1.data[0] == cursor2.data[0]:
                if cursor1.data[1] > cursor2.data[1]:
                    if cursor2.next.data is None:
                        return True
                    return cursor1.data[0] > cursor2.next.data[0]
                else:
                    if cursor1.next.data is None:
                        return False
                    return cursor1.next.data[0] > cursor2.data[0]
            return cursor1.data[0] > cursor2.data[0]

    def __ge__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        while cursor1.data == cursor2.data and cursor1.data is not None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1.data is None and cursor2.data is None:
            return True
        elif cursor1.data is None and cursor2.data is not None:
            return False
        elif cursor1.data is not None and cursor2.data is None:
            return True
        else:
            if cursor1.data[0] == cursor2.data[0]:
                if cursor1.data[1] > cursor2.data[1]:
                    if cursor2.next.data is None:
                        return True
                    return cursor1.data[0] > cursor2.next.data[0]
                else:
                    if cursor1.next.data is None:
                        return False
                    return cursor1.next.data[0] > cursor2.data[0]
            return cursor1.data[0] > cursor2.data[0]

    def __repr__(self):
        cursor = self.data.header.next
        str = ""
        while cursor.data is not None:
            str += cursor.data[0] * cursor.data[1]
            cursor = cursor.next
        return str