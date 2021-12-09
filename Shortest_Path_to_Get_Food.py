# You are starving and you want to eat food as quickly as possible. You want to find the shortest
# path to arrive at any food cell.
#
# You are given an m x n character matrix, grid, of these different types of cells:
#
# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.
#
# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food,
# return -1.
#
# Input: grid = [["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"], ["X", "O", "O", "#", "O", "X"],
#                ["X", "X", "X", "X", "X", "X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.
#
# Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.
#
# Input: grid =
# [["X","X","X","X","X","X","X","X"],
# ["X","*","O","X","O","#","O","X"],
# ["X","O","O","X","O","O","X","X"],
# ["X","O","O","O","O","#","O","X"],
# ["X","X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

from collections import deque

class Solution:
    def getFood(self, grid) -> int:
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "*":
                    queue.append((row, col, 0))

        while queue:

            row, col, res = queue.popleft()
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 'X':

                if grid[row][col] == '#':
                    return res
                grid[row][col] = 'X'
                for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newRow = rowOffset + row
                    newCol = colOffset + col
                    newState = (newRow, newCol, res + 1)
                    queue.append(newState)

        return -1