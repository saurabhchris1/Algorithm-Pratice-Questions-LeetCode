# Given the root of a binary tree, return the maximum width of the given tree.
#
# The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes),
# where the null nodes between the end-nodes are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of 32-bit signed integer.

# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
#
# Input: root = [1, 3, null, 5, 3]
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5, 3).
#
# Input: root = [1, 3, 2, 5]
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3, 2).

# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root) -> int:

        if not root:
            return None

        maxWidth = 0
        queue = deque([(root, 0)])

        while queue:
            level = len(queue)
            _, leftIdx = queue[0]
            for _ in range(level):
                node, colIdx = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * colIdx))
                if node.right:
                    queue.append((node.right, 2 * colIdx + 1))

            maxWidth = max(maxWidth, colIdx - leftIdx + 1)

        return maxWidth