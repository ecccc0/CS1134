# def remove_all(lst, value): 
#     end = False 
#     while(end == False): 
#         try: 
#             lst.remove(value) 
#         except ValueError: 
#             end = True
# Runtime: O(n^2) since remove is O(n) and it would take n removes to remove a list  
# containing many occuraances of value. e.g. [1, 2, 3, 4, 5, 5, 5, 5]

def remove_all(lst, value):
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == value:
            cnt += 1
        else:
            lst[i-cnt] = lst[i]
    for i in range(cnt):
        lst.pop()
    
# lst = [1, 2, 3, 4, 1, 1, 1, 1]
# remove_all(lst, 1)
# print(lst)
        
# Worst case O(n), the first iteration counts the occurances of the value and move the rest in O(1) time
# The second iteration removes the extra items (cnt # of them, cnt <= n) So in worst case where all
# values in lst is equal to value, the algorithm does 2n O(1) operations