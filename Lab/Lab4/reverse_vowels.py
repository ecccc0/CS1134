def reverse_vowels(input_str):
    lst = [c for c in input_str]
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    l = 0
    r = len(lst) - 1
    while l < r:
        if lst[l] not in vowels:
            l += 1
        if lst[r] not in vowels:
            r -= 1
        if lst[r] in vowels and lst[l] in vowels:
            lst[r], lst[l] = lst[l], lst[r]
            l += 1
            r -= 1
    return ''.join(lst)

