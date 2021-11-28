# Given two integer arrays preorder and inorder where preorder is the preorder traversal of
# a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):

        def helper(left, right):

            if left > right:
                return None

            rootVal = preorder[self.preidx]
            root = TreeNode(rootVal)
            self.preidx += 1

            root.left = helper(left, inorderMap[rootVal] - 1)
            root.right = helper(inorderMap[rootVal] + 1, right)

            return root

        self.preidx = 0
        inorderMap = {}

        for idx, num in enumerate(inorder):
            inorderMap[num] = idx

        return helper(0, len(preorder) - 1)