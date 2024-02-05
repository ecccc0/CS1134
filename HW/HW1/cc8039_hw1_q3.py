def sum_sqaures(n):
    sum = 0
    for i in range(n):
        sum += i*i
    return sum
n = 6

sum([i*i for i in range(n)])

def sum_odd_sqaures(n):
    sum = 0
    for i in range(n):
        if i%2 == 1:
            sum += i*i
    return sum

sum([i*i for i in range(n) if i % 2 == 1])