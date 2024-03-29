import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    def __init__(self):
       self.data = make_array(10)
       self.capacity = 10
       self.n = 0
       self.front_ind = None 
    
    def __len__(self):
        return self.n
    
    def is_empty(self):
        return len(self) == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]
    
    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[(self.front_ind + len(self) -1 ) % self.capacity]
    
    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data = new_data
        self.capacity = new_cap
        self.front_ind = 0

    def enqueue_first(self, elem):
        if (self.n == self.capacity):
           self.resize(self.capacity * 2)
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
        new_front = (self.front_ind - 1) % self.capacity
        self.front_ind = new_front
        self.data[self.front_ind] = elem
        self.n += 1

    def enqueue_back(self, elem):
        if (self.n == self.capacity):
           self.resize(self.capacity * 2)
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data[back_ind] = elem
        self.n += 1
         
    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > 10)):
            self.resize(self.capacity // 2)
        return value
    
    def dequeue_back(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        back_ind = (self.front_ind + len(self) - 1) % self.capacity
        value = self.data[back_ind]
        self.data[back_ind] = None
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > 10)):
            self.resize(self.capacity // 2)
        return value
        