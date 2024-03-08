def nestedSum(lst):
    sum = 0
    for i in range(len(lst)):
        if isinstance(lst[i], int):
            sum += lst[i]
        if isinstance(lst[i], list):
            sum += nestedSum(lst[i])
    return sum

print(nestedSum( [ [1, 2], 3, [4, [5, 6, [7], 8 ] ] ]))