def count_lowercase(s, low, high):
    if low > high:
        return 0
    prev = count_lowercase(s, low+1, high)
    if s[low].islower():
        return 1+prev
    else:
        return prev
    

def is_number_of_lowercase_even(s, low, high):
    if low > high:
        return True
    prev = is_number_of_lowercase_even(s, low+1, high)
    if s[low].islower():
        return not prev
    return prev
