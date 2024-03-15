from ArrayStack import *
class MeanStack():
    def __init__(self):
        self.data = ArrayStack()
        self.sum_val = 0.0
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self, e):
        if not (isinstance(e, int) or isinstance(e, float)):
            raise TypeError("not an integer or float")
        else:
            self.sum_val += e 
            self.data.push(e)
    def pop(self):
        if self.data.is_empty():
            raise Exception("Stack is empty")
        else:
            self.sum_val -= self.top()
            self.data.pop()
    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.data[-1]
    def sum(self):
        return self.sum_val
    def mean(self):
        return self.sum_val / len(self) if not self.is_empty() else 0
    
ms = MeanStack()
lst = [1, 2 ,3 ,4 ,5 ,6]
for x in lst:
    ms.push(x)
print(ms.sum())
print(ms.mean())