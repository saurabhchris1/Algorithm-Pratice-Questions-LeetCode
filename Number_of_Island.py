# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

class Solution:
    class Solution:
        def numIslands(self, grid):
            res = 0
            visited = set()
            for row in range(len(grid)):
                for col in range(len(grid[0])):

                    if grid[row][col] == "1" and (row, col) not in visited:
                        res += 1
                        self.dfs(row, col, grid, visited)

            return res

        def dfs(self, row, col, grid, visited):

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited:
                return

            if grid[row][col] != "1":
                return

            visited.add((row, col))

            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = rowOffset + row
                c = colOffset + col

                self.dfs(r, c, grid, visited)