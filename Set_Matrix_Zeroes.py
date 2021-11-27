# Given an m x n integer matrix matrix, if an element is 0, set its
# entire row and column to 0's, and return the matrix.
#
# You must do it in place.
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution:
    def setZeroes(self, matrix):

        rowSet = set()
        colSet = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                if r in rowSet:
                    matrix[r][c] = 0
                if c in colSet:
                    matrix[r][c] = 0
        return matrix