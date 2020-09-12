def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    row = 0
    col = 0
    goingDown = True
    res = []

    while not isOutOfBound(row, col, height, width):
        res.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1

            else:
                row += 1
                col -= 1

        else:

            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1

            else:
                row -= 1
                col += 1

    return res


def isOutOfBound(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width
