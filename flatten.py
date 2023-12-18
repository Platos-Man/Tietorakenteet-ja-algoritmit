def flatten(arr):
    l = []
    flag = False
    for e in arr:
        if isinstance(e, list):
            l += e
            flag = True
        else:
            l.append(e)
    if flag:
        return flatten(l)
    return l


print(flatten([1, 2, 3, [4, 5]]))  # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]]))  # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]]))  # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))  # [1, 2, 3]
