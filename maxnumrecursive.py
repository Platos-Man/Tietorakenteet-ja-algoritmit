def mnr(l, n):
    if n == 1:
        return l[0]
    return max(l[n - 1], mnr(l, n - 1))


def mnr2(l):
    if len(l) == 1:
        return l[0]
    return max(l[-1], mnr2(l[:-1]))


l = [5, 3, 9, 8, 12, 28, 6]
print(mnr(l, 7))
print(mnr2(l))
