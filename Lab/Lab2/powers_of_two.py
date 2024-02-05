def powers_of_two(n):
    for i in range(n):
        yield 2**i

for x in powers_of_two(6):
    print(x)