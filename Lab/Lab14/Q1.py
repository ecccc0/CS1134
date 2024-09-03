from ChainingHashTableMap import *
def most_frequent(lst):
    map = ChainingHashTableMap()
    for num in lst:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    max_val = 0
    max_key = -1
    for x in map:
        if map[x] > max_val:
            max_val = map[x]
            max_key = x
    return max_key

def first_unique(lst):
    map = ChainingHashTableMap()
    for num in lst:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    for x in map:
        if map[x] == 1:
            return x
        

lst = [5,9,2,9,0,5,9,7]
print(first_unique(lst))