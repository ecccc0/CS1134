from ArrayQueue import *
import copy
def flatten_lst(lst):
    q = ArrayQueue()
    flat = False
    tmp = copy.deepcopy(lst)
    while not flat:
        res = []
        flat = True
        for i in range(len(tmp)):
            q.enqueue(tmp[i])
        for i in range(len(q)):
            val = q.dequeue()
            if isinstance(val, list):
                flat = False
                for x in val:
                    res.append(x)
            else:
                res.append(val)
        tmp = res
    return tmp

print(flatten_lst( [  [ [ [ 0 ] ] ] ,  [ 1, 2 ] , 3,  [ 4,  [ 5, 6,  [ 7 ] ] , 8 ] , 9 ]))