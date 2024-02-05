import random
def create_permutation(n):
    lst = [-1] * n
    for i in range(n):
        while True:
            idx = random.randint(0, n-1)
            if lst[idx] == -1:
                lst[idx] = i
                break
    return lst

def scramble_word(word):
    idx_lst = create_permutation(len(word))
    tmp = [''] * len(word)
    for i in range(len(word)):
        tmp[i] = word[idx_lst[i]]
    return "".join(tmp)

word = "pokemon"
print("Unscramble the word:" + " ".join(list(scramble_word(word))))
times = 1
while True:
    print(f"Try #{times}: ")
    if input() == word:
        print("Yay, you got it!")
        break
    else:
        print("Wrong!")
        times += 1