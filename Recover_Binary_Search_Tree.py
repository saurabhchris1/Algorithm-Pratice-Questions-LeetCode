# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped
# by mistake. Recover the tree without changing its structure.
#
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
#
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):

        if not root:
            return root

        x = None
        y = None
        pred = None
        curr = root
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            if pred and pred.val > curr.val:
                y = curr
                if not x:
                    x = pred
                else:
                    break
            pred = curr
            curr = curr.right

        x.val, y.val = y.val, x.val