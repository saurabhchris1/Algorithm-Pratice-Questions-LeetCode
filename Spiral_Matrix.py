# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix):

        if len(matrix) == 0:
            return []

        startRow, endRow = 0, len(matrix) - 1
        startCol, endCol = 0, len(matrix[0]) - 1
        res = []

        while startRow <= endRow and startCol <= endCol:

            for col in range(startCol, endCol + 1):
                res.append(matrix[startRow][col])

            for row in range(startRow + 1, endRow + 1):
                res.append(matrix[row][endCol])

            for col in reversed(range(startCol, endCol)):

                if startRow == endRow:
                    break
                res.append(matrix[endRow][col])

            for row in reversed(range(startRow + 1, endRow)):

                if startCol == endCol:
                    break

                res.append(matrix[row][startCol])

            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1

        return res
