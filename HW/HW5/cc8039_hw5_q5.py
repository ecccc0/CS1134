from ArrayStack import *
from ArrayQueue import *
import copy
def permutations(lst):
    s = ArrayStack()
    q = ArrayQueue()
    for x in lst:
        s.push(x)
    for i in range(len(s)):
        cur = s.pop()
        if q.is_empty():
            q.enqueue([cur])
        else:
            for j in range(len(q)):
                old = q.dequeue()
                for k in range(len(old) + 1):
                    new = copy.copy(old)
                    new.insert(k, cur)
                    q.enqueue(new)
    return [q.dequeue() for i in range(len(q))]

# print(permutations([1,2,3]))
