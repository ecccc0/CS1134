def split_parity(lst, low, high):
    if low >= high:
        return
    if lst[low] % 2 == 0:
        split_parity(lst, low+1, high)
    elif lst[high] % 2 != 0:
        split_parity(lst, low, high-1)
    if lst[low] % 2 !=0 and lst[high] % 2 == 0:
        lst[low], lst[high] = lst[high], lst[low]
        split_parity(lst, low+1, high-1)

lst = [4,-5, 2, 3,-1,-6, 7, 9, 0]
split_parity(lst, 0 ,len(lst)-1)
print(lst)        