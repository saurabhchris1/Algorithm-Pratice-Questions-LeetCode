def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            isRowBorder = row == 0 or row == len(matrix) - 1
            isColBorder = col == 0 or col == len(matrix[0]) - 1
            isBorder = isRowBorder or isColBorder

            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue

            changeOnesConnectedToBorderToTwos(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            color = matrix[row][col]

            if color == 1:
                matrix[row][col] = 0
            elif color == 2:
                matrix[row][col] = 1

    return matrix


def changeOnesConnectedToBorderToTwos(matrix, row, col):
    stack = [(row, col)]

    while stack:
        currRow, currCol = stack.pop()
        matrix[currRow][currCol] = 2
        neighbours = getNeighbours(matrix, currRow, currCol)

        for neighbour in neighbours:
            row, col = neighbour

            if matrix[row][col] == 1:
                stack.append((row, col))


def getNeighbours(matrix, row, col):
    res = []

    if row + 1 < len(matrix):
        res.append((row + 1, col))
    if row - 1 >= 0:
        res.append((row - 1, col))
    if col + 1 < len(matrix[0]):
        res.append((row, col + 1))
    if col - 1 >= 0:
        res.append((row, col - 1))

    return res