def find_duplicates(lst):
    res = []
    cnt = [0 for i in range(len(lst) - 1)]
    for i in range(len(lst)):
        cnt[lst[i] - 1] += 1
    for i in range(len(cnt)):
        if cnt[i] > 1:
            res.append(i + 1)
    return res

# Worst Case: The runtime will always be 2n-1 (O(n))since we always traverse through
# the entire lst (length n) to create the cnt list, and we always traverse through 
# the entire cnt list (length n-1) to find duplicates