# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
#
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# Example 2:
#
# Input: root = [1], target = 4.428571
# Output: 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root, target):
        closest = float("inf")

        curr = root

        while curr:

            if abs(target - curr.val) < abs(target - closest):
                closest = curr.val

            if target > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        return int(closest)