# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:
#
# Input: root = [1]
# Output: ["1"]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root):
        res = []
        stack = [(root, str(root.val))]

        while stack:
            node, strs = stack.pop()

            if not node.left and not node.right:
                res.append(strs)

            if node.right:
                stack.append((node.right, strs + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, strs + "->" + str(node.left.val)))

        return res