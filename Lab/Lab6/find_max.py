# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#         # base case
#     prev = find_max(lst[1:])
#     if prev > lst[0]:
#         return prev
#     return lst[0]
# O(n^2)
def find_max(lst, low, high):
    if low == high:
        return lst[low]
    prev = find_max(lst, low+1, high)
    if lst[low] > prev:
        return lst[low]
    return prev

print(find_max([13, 9, 16, 3, 4, 2], 0, 5))