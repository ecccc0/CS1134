class Complex:
    def __init__(self, a, b):
        self.re = a
        self.im = b
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)
    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)
    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
    def __repr__(self):
        if self.im > 0:
            return f"{self.re} + {self.im}i"
        else:
            return f"{self.re} - {-self.im}i"
    def __iadd__(self, other):
        self.re += other.re
        self.im += other.im

cplx1 = Complex(5, 2)
print(cplx1) #5 + 2i
cplx2 = Complex(3, 3)
print(cplx2) #3 + 3i
#addition
print(cplx1 + cplx2) #8 + 5i
#subtraction
print(cplx1 - cplx2) #2 - 1i
#multiplication
print(cplx1 * cplx2)
print(cplx1) #5 + 2i
print(cplx2) #3 + 3i

