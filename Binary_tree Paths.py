# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        res = []

        def helper(node, path):

            if not node:
                return

            if not node.left and not node.right:
                res.append("->".join(path + [str(node.val)]))
                return

            helper(node.left, path + [str(node.val)])
            helper(node.right, path + [str(node.val)])

        helper(root, [])

        return res

    def binaryTreePathsIterative(self, root):
        res = []
        stack = [(root, [str(root.val)])]

        while stack:

            node, path = stack.pop()

            if not node.left and not node.right:
                res.append("->".join(path))

            if node.right:
                stack.append((node.right, path + [str(node.right.val)]))
            if node.left:
                stack.append((node.left, path + [str(node.left.val)]))

        return res
