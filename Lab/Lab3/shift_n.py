from reverse_list import reverse_list
def shift(lst, k):
    reverse_list(lst)
    reverse_list(lst, k-1, 0)
    reverse_list(lst, len(lst) - 1, k)

lst = [1, 2, 3, 4, 5, 6]
shift(lst, 2)
print(lst)
