def find_uniq(arr):
    if arr[0] == arr[1]:
        return [num for num in arr if num != arr[0]][0]
    else:
        if arr[0] == arr[2]:
            return [num for num in arr if num != arr[0]][0]
        else:
            return arr[0]
    # return n   # n: unique number in the array


def find_uniq2(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


print(find_uniq([1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3]))

print(find_uniq2([1, 1, 2, 1, 1]))
print(find_uniq2([0, 0, 0.55, 0, 0]))
print(find_uniq2([3, 10, 3, 3, 3]))
