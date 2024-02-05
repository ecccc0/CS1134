def fibs(n):
    x = 0
    y = 1
    for i in range(n):
        sum = x + y
        x = y
        yield y
        y = sum

# for curr in fibs(8):
#     print(curr)