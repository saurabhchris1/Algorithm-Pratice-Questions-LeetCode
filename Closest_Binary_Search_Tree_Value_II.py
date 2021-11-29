# Given the root of a binary search tree, a target value, and an integer k, return the k
# values in the BST that are closest to the target. You may return the answer in any order.
#
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
#
# Input: root = [4,2,5,1,3], target = 3.714286, k = 2
# Output: [4,3]
#
# Input: root = [1], target = 0.000000, k = 1
# Output: [1]

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq

class Solution:
    def closestKValues(self, root, target, k):

        heap = []
        stack = []
        curr = root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            heapq.heappush(heap, (-abs(curr.val - target), curr.val))

            if len(heap) > k:
                heapq.heappop(heap)

            curr = curr.right

        return [x for _, x in heap]