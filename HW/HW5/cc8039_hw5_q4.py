from ArrayStack import *
class Queue:
    def __init__(self):
        self.instack = ArrayStack()
        self.outstack = ArrayStack()
    
    def __len__(self):
        return len(self.instack) + len(self.outstack)
    
    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self, e):
        self.instack.push(e)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.instack.is_empty():
            val = self.outstack.pop()
        else:
            for i in range(len(self.instack)):
                self.outstack.push(self.instack.pop())
            val = self.outstack.pop()
        return val
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.instack.is_empty():
            return self.outstack.top()
        else:
            for i in range(len(self.instack)):
                self.outstack.push(self.instack.pop())
            return self.outstack.top()
        
    
