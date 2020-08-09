# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two
# nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#
#           1
#          / \
#         2   3
#        / \
#       4   5

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right + 1)

            return max(left, right) + 1

        depth(root)
        return self.ans - 1
