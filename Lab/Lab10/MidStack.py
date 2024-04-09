from DoublyLinkedList import *
class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = self.data.header

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.add_last(e)
        if len(self) % 2 == 1:
            self.mid = self.mid.next
    
    def top(self):
        if self.data.trailer.prev is self.data.header:
            raise Exception("empty stack")
        return self.data.trailer.prev.data
        
    def pop(self):
        if (len(self) - 1) % 2 == 0:
            self.mid = self.mid.prev
        return self.data.delete_last()
   
    def mid_push(self, e):
        if self.data.trailer.prev is self.data.header:
            raise Exception("empty stack")
        self.data.add_after(self.mid, e)

midS = MidStack()
midS.push(2)
midS.push(4)
midS.push(6)
midS.push(8)
midS.push(10)
midS.pop()
midS.mid_push(12)
print(midS.data)