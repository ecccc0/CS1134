def appearances(s, low, high):
    if low == high:
        return {s[low] : 1}
    dict = appearances(s, low+1, high)
    if s[low] not in dict:
        dict[s[low]] = 1
    else:
        dict[s[low]] += 1
    return dict

s = 'Hello, world'
print(appearances(s, 0, len(s)-1))