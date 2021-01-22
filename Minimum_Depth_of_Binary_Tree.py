# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 2


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = float("inf")
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)

        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1