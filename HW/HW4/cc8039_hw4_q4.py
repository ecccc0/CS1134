def list_min(lst, low, high):
    if low == high:
        return lst[low]
    prev = list_min(lst, low+1, high)
    if lst[low] < prev:
        return lst[low]
    return prev
