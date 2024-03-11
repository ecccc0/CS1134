def split_by_sign(lst, low, high):
    if low >= high:
        return
    if lst[low] < 0:
        split_by_sign(lst, low+1, high)
    if lst[high] > 0:
        split_by_sign(lst, low, high-1)
    if lst[low] > 0 and lst[high] < 0:
        lst[low], lst[high] = lst[high], lst[low]
        split_by_sign(lst, low+1, high-1)

# lst = [1, -1, 2, -3, 13,4, -12, 233,42, -1, -123, -13]
# split_by_sign(lst, 0, len(lst) - 1)
# print(lst)