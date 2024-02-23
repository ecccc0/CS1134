import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, it = -1):
        if it != -1 and hasattr(it, "__iter__"):
            self.data_arr = make_array(len(it) + 1)
            self.capacity = len(it) + 1
            self.n = len(it)
            for x in it:
                self.append(x)
        else:
            self.data_arr = make_array(1)
            self.capacity = 1
            self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if ind < 0:
            ind = len(self) - ind
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if ind < 0:
            ind = len(self) - ind
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        val = ", ".join(str(x) for x in self)
        return f"[{val}]"
    
    def __add__(self, other):
        res = ArrayList()
        for x in self:
            res.append(x)
        for x in other:
            res.append(x)
        return res

    def __iadd__(self, other):
        for x in other:
            self.append(x)
        return self
    
    def __mul__(self, k):
        res = ArrayList()
        for i in range(k):
            for x in self:
                res.append(x)
        return res
    
    def __rmul__(self, k):
        res = ArrayList()
        for i in range(k):
            for x in self:
                res.append(x)
        return res

    def remove(self, val):
        idx = -1
        for i in range(len(self)):
            if self[i] == val:
                idx = i
                break
        else:
            raise ValueError("Value not found")
        idx += 1
        while idx < len(self):
            self[idx - 1] = self[idx]
            idx += 1
        self.n -= 1
        
    def removeAll(self, val):
        insertPos = 0
        for i in range(len(self)):
            if self[i] != val:
                self[insertPos] = self[i]
                insertPos += 1
        
        self.n = insertPos



lst = ArrayList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(2)
lst.removeAll(1)
print(lst)