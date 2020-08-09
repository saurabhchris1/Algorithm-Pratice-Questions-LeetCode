# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flatten(self, root):
        self.flattenTree(root)

    def flattenTree(self, node):

        if not node:
            return None

        if not node.left and not node.right:
            return node

        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)

        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        return rightTail if rightTail else leftTail

    def iterative(self, root):

        if not root:
            return

        node = root

        while node:

            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = node.right
                node.right = node.left
                node.left = None

            node = node.right

    # def flatten(self, root):
    #     arr = []
    #     self.traverse(root, arr)
    #
    #     for i in range(len(arr) - 1):
    #         node1 = arr[i]
    #         node2 = arr[i + 1]
    #         node1.right = node2
    #         node1.left = None
    #     return root
    #
    # def traverse(self, node, arr):
    #
    #     if node is not None:
    #         arr.append(node)
    #         self.traverse(node.left, arr)
    #         self.traverse(node.right, arr)
