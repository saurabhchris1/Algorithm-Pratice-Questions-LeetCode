# Given the root of a binary tree, return the vertical order traversal of its nodes'
# values. (i.e., from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
#
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
#
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root):

        if not root:
            return []

        queue = deque([(0, root)])
        dict = defaultdict(list)
        minColIdx = float("inf")
        maxColIdx = float("-inf")
        res = []

        while queue:
            level = len(queue)

            for _ in range(level):
                col, node = queue.popleft()
                dict[col].append(node.val)
                minColIdx = min(minColIdx, col)
                maxColIdx = max(maxColIdx, col)
                if node.left:
                    queue.append((col - 1, node.left))

                if node.right:
                    queue.append((col + 1, node.right))

        for key in range(minColIdx, maxColIdx + 1):
            res.append(dict[key])

        return res