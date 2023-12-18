def chess_board(num):
    i = 0
    while i < num:
        row = ""
        n = 0
        while n < num:
            if i % 2 == 0:
                if n % 2 == 0:
                    row += "1"
                else:
                    row += "0"
            else:
                if n % 2 == 0:
                    row += "0"
                else:
                    row += "1"
            n += 1
        i += 1
        print(row)


def chess_board2(num):
    i = 0
    while i < num:
        if i % 2 == 0:
            symbol = "10"
        else:
            symbol = "01"

        if num % 2 == 0:
            row = symbol * (num // 2)
        else:
            row = (symbol * (num // 2 + 1))[:num]
        i += 1
        print(row)


chess_board2(7)
