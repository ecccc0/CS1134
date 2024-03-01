def product_evens(n):
    if n == 2:
        return 2
    return n * product_evens(n - 2)

print(product_evens(6))