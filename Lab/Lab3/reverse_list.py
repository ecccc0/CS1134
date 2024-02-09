def reverse_list(lst, high = None, low = None):
    if high is not None:
        hi = high
    else:
        hi = len(lst) - 1
    if low is not None:
        lo = low
    else:
        lo = 0
    while hi > lo:
        lst[hi], lst[lo] = lst[lo], lst[hi]
        hi -= 1
        lo += 1

# lst = [1,2,3,4,5,6]
# reverse_list(lst, 3, 1)
# print(lst)