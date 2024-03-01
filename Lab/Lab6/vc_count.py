def vc_count(word, low, high):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if low > high:
        return (0, 0)
    prev = vc_count(word, low+1, high)
    if word[low].lower() in vowels:
        return (1+prev[0], 0+prev[1])
    elif word[low].isalpha():
        return (0+prev[0], 1+prev[1])

s = "NYUTandonEngineering"
print(vc_count(s, 0, len(s) - 1))