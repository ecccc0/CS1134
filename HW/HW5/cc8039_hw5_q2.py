from ArrayStack import *
class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def top(self):
        if len(self) == 0:
            raise Exception("MaxStack is empty")
        return self.data.top()[0]
    
    def push(self, e):
        if self.is_empty() or self.data.top()[1] < e:
            self.data.push((e, e))
        else:
            self.data.push((e, self.data.top()[1]))

    def pop(self):
        if len(self) == 0:
            raise Exception("MaxStack is empty")
        return self.data.pop()[0]
    
    def max(self):
        if len(self) == 0:
            raise Exception("MaxStack is empty")
        return self.data.top()[1]
    
# maxS = MaxStack()
# maxS.push(3)
# maxS.push(1)
# maxS.push(6)
# maxS.push(4)
# print(maxS.max())
# print(maxS.pop())
# print(maxS.pop())
# print(maxS.max())

