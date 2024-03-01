def is_palindrome(str, low, high):
    if low >= high:
        return True
    if str[low] != str[high]:
        return False
    return is_palindrome(str, low+1, high-1)

print(is_palindrome("racecar", 1, 5))