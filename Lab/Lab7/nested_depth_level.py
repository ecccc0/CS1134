def nested_depth_level(lst):
    depth = 1
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            cur = 1 + nested_depth_level(lst[i])
            depth = max(depth, cur)
    return depth

lst = [ [1, 2], 3, [4, [5, 6, [7], 8 ] ], [ [ [ [9] ] ] ] ]
print(nested_depth_level(lst))