from ArrayStack import *
def flatten_lst(lst):
    s = ArrayStack()
    flat = False
    while not flat:
        flat = True
        for i in range(len(lst)):
            s.push(lst.pop())
        for i in range(len(s)):
            val = s.pop()
            if isinstance(val, list):
                flat = False
                for x in val:
                    lst.append(x)
            else:
                lst.append(val)
        


lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]    
flatten_lst(lst)
print(lst)