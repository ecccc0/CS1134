def can_construct(word , letters):
    """
    word - type: str
    letters - type: str
    return value - type: bool
    """
    lst_dict_word = [0]*26
    lst_dict_letters = [0]*26
    for i in range(len(word)):
        lst_dict_word[ord(word[i]) - 97] += 1
    for i in range(len(letters)):
        lst_dict_letters[ord(letters[i]) - 97] += 1
    for i in range(len(lst_dict_word)):
        if lst_dict_word[i] > lst_dict_letters[i]:
            return False
    return True

print(can_construct("apples", "aplespl"))