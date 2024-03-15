from ArrayStack import *

def stack_sum(s):
    if len(s) == 0:
        return 0
    cur = s.top()
    ret = s.pop() + stack_sum(s)
    s.push(cur)
    return ret

s = ArrayStack()
lst = [1,-14, 5, 6,-7, 9, 10,-5,-8]
for x in lst:
    s.push(x)
print(stack_sum(s))
print(len(s))