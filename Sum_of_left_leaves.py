# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Iterative
    def sumOfLeftLeaves(self, root):

        if not root:
            return 0

        stack = [root]
        res = 0
        while stack:
            node = stack.pop()

            if self.isLeaf(node.left):
                res += node.left.val

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return res

    def isLeaf(self, node):
        return node is not None and not node.left and not node.right

    def sum_of_Left_Leaves_recurssive(self, root):
        if not root:
            return 0

        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
