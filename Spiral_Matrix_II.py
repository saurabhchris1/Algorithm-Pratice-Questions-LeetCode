# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    def generateMatrix(self, n):

        matrix = []
        for i in range(n):
            matrix.append([0] * n)

        startRow, endRow = 0, len(matrix) - 1
        startCol, endCol = 0, len(matrix[0]) - 1
        count = 1

        while startRow <= endRow and startCol <= endCol:

            for col in range(startCol, endCol + 1):
                matrix[startRow][col] = count
                count += 1

            for row in range(startRow + 1, endRow + 1):
                matrix[row][endCol] = count
                count += 1

            for col in reversed(range(startCol, endCol)):

                if startRow == endRow:
                    break
                matrix[endRow][col] = count
                count += 1

            for row in reversed(range(startRow + 1, endRow)):

                if startCol == endCol:
                    break

                matrix[row][startCol] = count
                count += 1

            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1

        return matrix
