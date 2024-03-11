def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    res = []
    for i in range(high - low + 1):
        for per in permutations(lst, low+1, high):
            per.insert(i, lst[low])
            res.extend([per])
    return res

