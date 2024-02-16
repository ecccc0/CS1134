# def find_missing(lst):
#     for num in range(len(lst) + 1):
#         if num not in lst:
#           return num
#  O(n^2)

# 0, 1, 3, 4, 5, 6, 7, 8
# 0, 1, 2, 3, 4, 5, 6, 8
def find_missing(lst):
    # edge cases>
    if lst[0] != 0:
        return 0
    if lst[-1] != len(lst):
        return len(lst)
    l = 0
    r = len(lst) - 1
    while l < r:
        if l + 1 == r:
            return l+1
        mid = (l + r) // 2
        if lst[mid] == mid:
            l = mid
        elif lst[mid] != mid:
            r = mid

# print(find_missing([0, 2]))
            
def find_missing_unsorted(lst):
    sum = ((len(lst)+1) * len(lst)) // 2
    for x in lst:
        sum -= x
    return sum
# print(find_missing_unsorted([1, 2, 3, 4, 5]))