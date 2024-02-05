class Polynomial:
    def __init__(self, coefficients=[0]):
        self.coefficients = coefficients
    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        res = []
        for i in range(max_len):
            if i >= len(self.coefficients):
                res.append(other.coefficients[i])
            elif i >= len(other.coefficients):
                res.append(self.coefficients[i])
            else:
                res.append(self.coefficients[i] + other.coefficients[i])
        return Polynomial(res)
    def __call__(self, param):
        res = 0
        for i in range(len(self.coefficients)):
            res += (param ** i) * self.coefficients[i]
        return res
    def __repr__(self):
        res = " + ".join([f"{self.coefficients[i]}x^{i}" for i in range(len(self.coefficients)-1, 0, -1)if self.coefficients[i] != 0])
        if self.coefficients[0] != 0:
            res +=  f" + {self.coefficients[0]}"
        return res
    def __mul__(self, other):
        highest_power = (len(self.coefficients)) + (len(other.coefficients))
        res = [0] * highest_power
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                res[i+j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(res)
    def derive(self):
        if len(self.coefficients) == 1:
            self.coefficients = [0]
            return None
        res = [0] * (len(self.coefficients) - 1)
        for i in range(len(res)):
            res[i] = (i+1) * self.coefficients[i+1]
        self.coefficients = res
    
poly1 = Polynomial([3, 7, 0, -9, 2]); # represents 2x4 - 9x3 + 7x + 3
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3]); # represents 3x6 + 5x3 + 2
poly3 = poly1 + poly2
print(poly3.coefficients) # return [5, 7, 0, -4, 2, 0, 3]
print(poly1(1)) # return 3
print(poly2(1)) # return 10
print(poly3(1)) # return 13
# Optional test values
poly1.derive() # returns none
print(poly1) # returns '8x^3 + -27x^2 + 7’
print(poly1.coefficients)
poly4 = poly1 * Polynomial([1,2])
print(poly4) # return array of 8x3 -27x2 + 7 * (2x + 1)