# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return root

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

        # def helper(root, res):
        #     if not root:
        #         return res
        #     res.append(root.val)
        #     helper(root.left, res)
        #     helper(root.right, res)
        #
        #     return res
        # return helper(root, [])