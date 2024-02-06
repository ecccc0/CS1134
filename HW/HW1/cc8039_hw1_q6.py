class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0]*d
        else:
            self.coords = d
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        return Vector([self[i] + other[i] for i in range(len(self))])
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'
    def __repr__(self):
        return str(self)
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimentions must agree")
        return Vector([self[i] - other[i] for i in range(len(self))])
    def __neg__(self):
        return Vector([-item for item in self])
    def __mul__(self, x):
        if isinstance(x, int):
            return Vector([item*x for item in self])
        elif len(x) == len(self):
            return sum([self[i] * x[i] for i in range(len(self))])
        else:
            raise ValueError("dimesntions must agree")
    def __rmul__(self, x):
        return Vector([i * x for i in self])


# v1 = Vector(5)
# v1[1] = 10
# v1[-1] = 10
# print(v1)
# v2 = Vector([2, 4, 6, 8, 10])
# print(v2)

# u1 = v1 + v2
# print(u1)
# u2 = -v2
# print(u2)
# u3 = 3 * v2
# print(u3)
# u4 = v2 * 3
# print(u4)
# u5 = v1 * v2
# print(u5)