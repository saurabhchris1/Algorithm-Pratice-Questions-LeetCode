# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.


class Solution:

    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        seen = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    currentMax = 0
                    stack = []
                    stack.append((row, col))

                    while stack:
                        r, c = stack.pop()
                        if grid[r][c] == 1 and (r, c) not in seen:
                            currentMax += 1
                            seen.add((r, c))
                            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                            for d in directions:
                                newRow = r + d[0]
                                newCol = c + d[1]
                                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                                    stack.append((newRow, newCol))

                    maxArea = max(maxArea, currentMax)
        return maxArea

    # def maxAreaOfIsland(self, grid):
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     maxArea = 0
    #     for row in range(rows):
    #         for col in range(cols):
    #             currentMax = 0
    #             if grid[row][col] == 1:
    #                 currentMax = self.findArea(grid, row, col, currentMax)
    #
    #             maxArea = max(maxArea, currentMax)
    #     return maxArea
    #
    # def findArea(self, grid, row, col, currentMax):
    #     if grid[row][col] == 1:
    #         currentMax += 1
    #         grid[row][col] = 0
    #     else:
    #         return currentMax
    #
    #     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    #
    #     for d in directions:
    #         r = row + d[0]
    #         c = col + d[1]
    #
    #         if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
    #             currentMax = self.findArea(grid, r, c, currentMax)
    #
    #     return currentMax