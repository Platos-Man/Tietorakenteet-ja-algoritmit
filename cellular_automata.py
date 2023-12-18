def get_generation(cells : list[list[int]], generations : int) -> list[list[int]]:

    for _ in range(generations):
        cells = create_outer_rim(cells)
        for y, row in enumerate(cells):
            for x, col in enumerate(row):
                neighbour = 0

        for row in cells:
            print(row)
        cells = remove_outer_rim(cells)
        
        for row in cells:
            print(row)
    
    return []

def create_outer_rim(cells):
    for row in cells:
        row.insert(len(row), 0)
        row.insert(0, 0)
    cells.insert(len(cells), [0]*len(cells[0]))
    cells.insert(0, [0]*len(cells[0]))
    
    return cells

def remove_outer_rim(cells):
    if not 1 in cells[0]:
        cells.pop(0)
    if not 1 in cells[-1]:
        cells.pop(-1)

    left = False
    right = False

    for row in cells[1:-1]:
        if not row[0]:
            left = True
        if not row[-1]:
            right = True
    
    for row in cells:
        if left:
            row.pop(0)
        if right:
            row.pop(-1)

    print()
    return cells

if __name__ == "__main__":
    cells = [
            [1,0,0],
            [0,1,1],
            [1,1,0]
        ]
    get_generation(cells, 1)

                # if cells[y-1][x-1]:
                #     neighbour += 1
                #     print(cells[y-1][x-1])

                # if cells[y][x-1]:
                #     neighbour += 1
                #     print(cells[y][x-1])

                # if cells[y+1][x-1]:
                #     neighbour += 1
                #     print(cells[y+1][x-1])

                # if cells[y-1][x]:
                #     neighbour += 1
                #     print(cells[y-1][x])

                # if cells[y+1][x]:
                #     neighbour += 1
                #     print(cells[y+1][x])

                # if cells[y-1][x+1]:
                #     neighbour += 1
                #     print(cells[y-1][x+1])

                # if cells[y][x+1]:
                #     neighbour += 1
                #     print(cells[y][x+1])

                # if cells[y+1][x+1]:
                #     neighbour += 1
                #     print(cells[y+1][x+1])