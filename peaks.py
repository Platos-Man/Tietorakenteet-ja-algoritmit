def pick_peaks(arr):
    obj = {"pos": [], "peaks": []}
    memory = {"pos": None, "peak": None}
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            memory["pos"] = i
            memory["peak"] = arr[i]
        elif arr[i] < arr[i - 1] and not memory["pos"] == None:
            obj["pos"].append(memory["pos"])
            obj["peaks"].append(memory["peak"])
            memory["pos"] = None

    return obj


print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]))

# {"pos":[3,7,10], "peaks":[6,3,2]}
print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))

# {"pos":[3,7], "peaks":[6,3]}
print(
    pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3])
)
# {"pos":[2,7,14,20], "peaks":[5,6,5,5]}
