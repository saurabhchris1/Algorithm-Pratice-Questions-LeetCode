# Given an array of integers preorder, which represents the preorder traversal of a BST
# (i.e., binary search tree), construct the tree and return its root.
#
# It is guaranteed that there is always possible to find a binary search tree with the
# given requirements for the given test cases.
#
# A binary search tree is a binary tree where for every node, any descendant of Node.left
# has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
#
# A preorder traversal of a binary tree displays the value of the node first, then traverses
# Node.left, then traverses Node.right.

# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# Example 2:
#
# Input: preorder = [1,3]
# Output: [1,null,3]

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorderRecursive(self, preorder):
        self.idx = 0

        def helper(lower, upper):

            if self.idx == len(preorder):
                return None

            val = preorder[self.idx]

            if val > upper or val < lower:
                return None

            self.idx += 1

            node = TreeNode(val)
            node.left = helper(lower, val)
            node.right = helper(val, upper)

            return node

        return helper(float("-inf"), float("inf"))