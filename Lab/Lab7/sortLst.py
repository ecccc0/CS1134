def sortLst(lst):
    cnt = [0] * len(lst)
    for x in lst:
        cnt[x] += 1
    idx = 0
    for i in range(len(cnt)):
        while cnt[i] > 0:
            lst[idx] = i
            idx += 1
            cnt[i] -= 1

lst = [2,0,2,1,1,2]
sortLst(lst)
print(lst)