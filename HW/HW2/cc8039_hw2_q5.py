# 1 2 3 4
# 
def split_parity(lst):
    l = 0
    r = len(lst) - 1
    while l < r and lst[l] % 2 != 0:
        l += 1
    while l < r and lst[r] % 2 == 0:
        r -= 1
    while l < r:
        lst[l], lst[r] = lst[r], lst[l]
        while l < r and lst[l] % 2 != 0:
            l += 1
            print(l)
        while l < r and lst[r] % 2 == 0:
            r -= 1

# lst = [1, 1, 1, 1]
# split_parity(lst)
# print(lst)