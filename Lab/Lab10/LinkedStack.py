import DoublyLinkedList
class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def push(self, e):
        self.data.add_last(e)
    def top(self):
        if self.data.trailer.prev is self.data.header:
            raise Exception("empty stack")
        return self.data.trailer.prev.data
    def pop(self):
        return self.data.delete_last()

ls = LinkedStack()
ls.push(1)
ls.push(2)
ls.push(3)
ls.push(4)
print(ls.data)
print(ls.pop())
print(ls.data)
print(len(ls))