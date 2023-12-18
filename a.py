def solution(number):
    number = number - 1
    if number < 1:
        return 0
    if number % 3 == 0 or number % 5 == 0:
        return number + solution(number)
    else:
        return solution(number)


# for i in range(-10000, 10000):
#     try:
#         solution(i)
#     except:
#         print(i)
print(solution(10000))
