from ChainingHashTableMap import *
def two_sum(lst, target):
    map = ChainingHashTableMap()
    for i in range(len(lst)):
        if lst[i] in map:
            return (map[lst[i]], i)
        map[target - lst[i]] = i
    return (None, None)