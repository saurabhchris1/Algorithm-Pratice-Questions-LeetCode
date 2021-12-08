# Given two integer arrays inorder and postorder where inorder is the inorder traversal
# of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
#
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        inorderMap = {}
        for idx, val in enumerate(inorder):
            inorderMap[val] = idx

        def helper(left, right):
            if left > right:
                return

            val = postorder.pop()
            node = TreeNode(val)

            node.right = helper(inorderMap[val] + 1, right)
            node.left = helper(left, inorderMap[val] - 1)

            return node

        root = helper(0, len(inorder) - 1)
        return root
