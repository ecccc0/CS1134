# [-2, 7, 11, 15, 20, 21] 22
def two_sum(srt_lst, target):
    l = 0
    r = len(srt_lst) - 1
    while l < r:
        if srt_lst[l] + srt_lst[r] == target:
            return (l, r)
        if srt_lst[l] + srt_lst[r] < target:
            l += 1
        else:
            r -= 1
    return None

# print(two_sum([10, 11, 11, 13], 22))