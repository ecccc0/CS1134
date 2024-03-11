def appearances(s, low, high):
    if low > high:
        return {}
    else:
        cur = s[low]
        dict = appearances(s, low + 1, high)
        
        if cur in dict:
            dict[cur] += 1
        else:
            dict[cur] = 1
        
        return dict

# s = 'Hello, world'
# print(appearances(s, 0, len(s)-1))