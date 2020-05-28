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
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        queue.append((-1, -1))
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        print(queue)
        while queue:
            print (queue)
            row, col = queue.popleft()

            if row == -1:
                minutes_elapsed += 1
                if queue:
                    queue.append((-1, -1))



            else:
                for d in directions:
                    neighbour_row, neighbour_col = row + d[0], col + d[1]

                    if rows > neighbour_row >= 0 and cols > neighbour_col >= 0:

                        if grid[neighbour_row][neighbour_col] == 1:
                            grid[neighbour_row][neighbour_col] = 2
                            fresh -= 1
                            queue.append((neighbour_row, neighbour_col))

        return minutes_elapsed if fresh == 0 else -1


if __name__ == "__main__":
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print (Solution().reqTme(grid1))