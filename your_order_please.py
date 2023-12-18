def order(sentence):
    if not sentence:
        return sentence
    arr = sentence.split()
    new_arr = []
    for i in range(1, len(arr) + 1):
        for word in arr:
            if str(i) in word:
                new_arr.append(word)

    return " ".join(new_arr)


def order2(sentence):
    return " ".join(sorted(sentence.split(), key=min))


print(min("Fo1r"))

print(order("4of Fo1r pe6ople g3ood th5e the2"))
