def max_sum_subarray(lst, k):
    cur = sum(lst[:k])
    res = cur
    i = 0
    j = k
    while i < len(lst) - k:
        cur -= lst[i]
        cur += lst[j]
        res = max(cur, res)
        i += 1
        j += 1
    return res
print(max_sum_subarray([1,12,-5,-6,50,3], 3))


