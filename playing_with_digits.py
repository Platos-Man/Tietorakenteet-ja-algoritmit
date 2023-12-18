def dig_pow(n, p):
    n_list = [int(num) for num in list(str(n))]
    total = 0
    for idx, num in enumerate(n_list):
        total += num ** (idx + p)
    k = int(total / n)
    if k * n == total:
        return k
    return -1


print(dig_pow(695, 2))
