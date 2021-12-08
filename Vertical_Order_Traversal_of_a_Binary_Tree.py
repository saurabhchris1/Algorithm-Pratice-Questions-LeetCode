# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
#
# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1)
# and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
#
# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting
# from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same
# column. In such a case, sort these nodes by their values.
#
# Return the vertical order traversal of the binary tree.
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
#           1 is at the top, so it comes first.
#           5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.

# Definition for a binary tree node.

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):

        if not root:
            return []

        sortedList = []

        def bfs(node):
            queue = deque([(0, 0, node)])

            while queue:
                level = len(queue)
                for _ in range(level):
                    row, col, node = queue.popleft()
                    sortedList.append((col, row, node.val))
                    if node.left:
                        queue.append((row + 1, col - 1, node.left))
                    if node.right:
                        queue.append((row + 1, col + 1, node.right))

        bfs(root)
        sortedList.sort()

        column = defaultdict(list)

        for col, row, val in sortedList:
            column[col].append(val)

        return column.values()