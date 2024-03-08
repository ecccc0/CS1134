def isPowerOfTwo(n):
    if n == 2:
        return True
    if n % 2 != 0:
        return False
    return isPowerOfTwo(n//2)

print(isPowerOfTwo(1024))