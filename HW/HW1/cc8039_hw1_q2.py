# def shift(lst, k):
#     tmp = lst[:k]
#     for i in range(len(lst) - k):
#         lst[i] = lst[i+k]
#     for i in range(len(lst) - k, len(lst)):
#         lst[i]=tmp[i-len(lst)+k]

# lst = [1, 2, 3, 4, 5, 6]
# shift(lst, 0)
# print(lst)

def shift(lst, k, dir="left"):
    if dir == "left":
        tmp = lst[:k]
        for i in range(len(lst) - k):
            lst[i] = lst[i+k]
        for i in range(len(lst) - k, len(lst)):
            lst[i]=tmp[i-len(lst)+k]
    else:
        # 1, 2, 3, 4, 5, 6 -> 5, 6, 1, 2, 3, 4
        tmp = lst[len(lst) - k:]
        for i in range(len(lst) - 1, k-1, -1):
            lst[i] = lst[i-k]
        for i in range(0, k):
            lst[i]=tmp[i]
# lst = [1, 2, 3, 4, 5, 6]
# shift(lst, 5, "right")
# print(lst)