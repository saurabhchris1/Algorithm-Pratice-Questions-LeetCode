# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange
# becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1 instead.
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten,
# because rotting only happens 4-directionally.
# Example 3:
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


from collections import deque


class Solution:

    def reqTme(self, grid):
        queue = collections.deque([])
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        mins = 0

        while queue and fresh:

            currNums = len(queue)
            mins += 1

            for _ in range(currNums):
                rottenMango = queue.popleft()

                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                for d in directions:
                    row = rottenMango[0] + d[0]
                    col = rottenMango[1] + d[1]

                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            fresh -= 1
                            queue.append((row, col))

        return -1 if fresh > 0 else mins


if __name__ == "__main__":
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print (Solution().reqTme(grid1))