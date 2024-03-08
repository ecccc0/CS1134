def intersectionOfList(lst1, lst2):
    res = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] == lst2[idx2]:
            res.append(lst1[idx1])
            idx1 += 1
            idx2 += 1
        elif lst1[idx1] > lst2[idx2]:
            idx2 += 1
        elif lst1[idx1] < lst2[idx2]:
            idx1 += 1
    return res

lst1 = [1,2,3,4]
lst2 = [3,4,5]
print(intersectionOfList(lst1, lst2))