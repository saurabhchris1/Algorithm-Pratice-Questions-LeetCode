# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        leftToRight = True
        current = collections.deque()
        res = []
        while queue:

            num = len(queue)

            for _ in range(num):
                node = queue.popleft()
                if leftToRight:
                    current.append(node.val)

                else:
                    current.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(current)
            leftToRight = not leftToRight
            current = collections.deque()

        return res
