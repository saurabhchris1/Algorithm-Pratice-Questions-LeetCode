# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root
        count = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right

        return None