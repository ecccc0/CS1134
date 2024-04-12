from ArrayDeque import *
from ArrayStack import *
class MidStack:
    def __init__(self):
        self.left = ArrayStack()
        self.right = ArrayDeque()

    def __len__(self):
        return len(self.left) + len(self.right)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        if self.is_empty():
            self.left.push(e)
        elif len(self.right) < len(self.left):
            self.right.enqueue_last(e)
        else:
            self.left.push(self.right.dequeue_first())
            self.right.enqueue_last(e)
    
    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        elif self.right.is_empty():
            return self.left.top()
        else:
            return self.right.last()
    
    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        elif self.right.is_empty():
            return self.left.pop()
        else:
            val = self.right.dequeue_last()
            if len(self.left) == len(self.right) + 1:
                return val
            else:
                self.right.enqueue_first(self.left.pop())
                return val
            
    def mid_push(self, e):
        if len(self.left) == len(self.right):
            self.left.push(e)
        else:
            self.right.enqueue_first(e)
    

# midS = MidStack()
# midS.push(2)
# midS.push(4)
# midS.push(6)
# midS.push(8)
# midS.push(10)
# midS.mid_push(12)
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())


