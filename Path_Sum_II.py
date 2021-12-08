# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
# values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
#
# Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
# Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum: int):
        res = []
        self.helper(root, targetSum, [], res)
        return res

    def helper(self, node, targetSum, arr, res):

        if not node:
            return

        arr.append(node.val)
        if not node.left and not node.right:
            if sum(arr) == targetSum:
                res.append(list(arr))
        else:
            self.helper(node.left, targetSum, arr, res)
            self.helper(node.right, targetSum, arr, res)

        arr.pop()