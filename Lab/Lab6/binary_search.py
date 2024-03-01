def binary_search(lst, low, high, val):
    mid = (low + high) // 2
    if low > high:
        return None
    if high == mid:
        return high
    if lst[mid] < val:
        return binary_search(lst, mid+1, high, val)
    else:
        return binary_search(lst, low, mid, val)
    
print(binary_search([1, 3, 6, 7, 10, 12, 14, 15, 20, 21], 0, 9, 20))
