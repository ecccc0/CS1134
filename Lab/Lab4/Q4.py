# 15, 20, 21, 22, 1, 2, 3, 6, 7, 10, 12
def find_pivot(lst):
    l = 0
    r = len(lst) - 1
    while l < r:
        mid = (l + r) // 2
        if lst[l] > lst[mid]:
            r = mid - 1
        else:
            l = mid + 1
        if lst[l - 1] > lst[l]:
            return l
        if r < len(lst)-1 and lst[r + 1] < lst[r]:
            return r+1
    return 0

def shift_binary_search(lst, target):
    pivot = find_pivot(lst)
    if target > lst[-1]:
        l = 0
        r = pivot - 1
    else:
        l = pivot
        r = len(lst) - 1

    while l < r:
        mid = (l + r) // 2 
        if (lst[mid] < target):
            l = mid + 1
        else:
            r = mid
    if lst[r] == target:
        return r
    return -1

lst = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]
print(shift_binary_search(lst , 12))