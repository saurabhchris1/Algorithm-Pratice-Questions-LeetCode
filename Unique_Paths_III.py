# You are given an m x n integer array grid where grid[i][j] could be:
#
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
#
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.


class Solution:
    def uniquePathsIII(self, grid):
        nonObstacle = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] >= 0:
                    nonObstacle += 1
                if grid[row][col] == 1:
                    startRow, startCol = row, col
        self.paths = 0

        def backtrack(row, col, remain):

            if grid[row][col] == 2 and remain == 1:
                self.paths += 1
                return

            temp = grid[row][col]
            grid[row][col] = -4
            remain -= 1
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = d[0] + row
                c = d[1] + col

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] >= 0:
                        backtrack(r, c, remain)

            grid[row][col] = temp

        backtrack(startRow, startCol, nonObstacle)
        return self.paths