# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
# sequence has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root) -> int:
        def maxPath(node):
            nonlocal maxVal
            if not node:
                return 0

            leftGain = max(maxPath(node.left), 0)
            rightGain = max(maxPath(node.right), 0)

            rootPath = node.val + leftGain + rightGain

            maxVal = max(maxVal, rootPath)

            return node.val + max(leftGain, rightGain)

        maxVal = -float("inf")
        maxPath(root)
        return maxVal