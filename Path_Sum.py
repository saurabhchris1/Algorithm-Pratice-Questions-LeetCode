# Given the root of a binary tree and an integer targetSum, return true if the tree has
# a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
# Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
# Output: true
# Explanation: The root - to - leaf path with the target sum is shown.
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree: (1 --> 2):
# The sum is 3. (1 --> 3): The sum is 4. There is no root-to-leaf path with sum = 5.
#
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):

        self.isAvailable = False

        def helper(node, pathSum):

            if not node:
                return

            pathSum += node.val

            if not node.left and not node.right:
                if pathSum == targetSum:
                    self.isAvailable = True
                return

            helper(node.left, pathSum)
            helper(node.right, pathSum)

        helper(root, 0)

        return self.isAvailable

    # self.isAvailable = False
    #
    # def helper(node, path):
    #     nonlocal targetSum
    #     if not node:
    #         return
    #     path.append(node.val)
    #     if not node.left and not node.right:
    #         if sum(path) == targetSum:
    #             self.isAvailable = True
    #     else:
    #         helper(node.left, path)
    #         helper(node.right, path)
    #
    #     path.pop()
    #
    # helper(root, [])
    # return self.isAvailable