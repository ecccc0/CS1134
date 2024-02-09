def move_zeroes(lst):
    i = 0
    j = 0
    while i < len(lst):
        if lst[i] == 0:
            j = i
            while j < len(lst):
                if lst[j] != 0:
                    lst[i], lst[j] = lst[j], lst[i]
                    break
                j += 1
        i += 1

lst = [0, 0, 0, 0, 1]
move_zeroes(lst)
print(lst)