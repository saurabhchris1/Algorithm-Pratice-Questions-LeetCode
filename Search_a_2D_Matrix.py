# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false


class Solution:
    def searchMatrix(self, matrix:, target):

        m = len(matrix)

        if m == 0:
            return False

        n = len(matrix[0])
        low = 0
        high = m * n - 1

        while low <= high:

            pivot = low + (high - low) // 2
            row = pivot // n
            col = pivot % n
            num = matrix[row][col]

            if target == num:
                return True
            elif target < num:
                high = pivot - 1
            else:
                low = pivot + 1

        return False
