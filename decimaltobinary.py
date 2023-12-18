def dtb(n):
    if n // 2 == 0:
        return str(n % 2)
    return dtb(n // 2) + str(n % 2)


def dtb2(n):
    if n // 2 == 0:
        return n % 2
    return n % 2 + 10 * dtb2(n // 2)


print(dtb2(10))


# for i in range(1, 101):
#     print(i, dtb(i))
