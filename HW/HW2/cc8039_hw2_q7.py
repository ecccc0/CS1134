# [0, 0, 0, 0, 0, 1, 1, 1]

def findChange(lst01):
    l = 0
    r = len(lst01) - 1
    while l < r:
        mid = (l + r) // 2
        if lst01[l] == 0 and lst01[mid] == 0:
            l = mid + 1
        else:
            r = mid
    return r

# print(findChange([0, 0, 0, 1]))