# You are given a perfect binary tree where all leaves are on the
# same level, and every parent has two children. The binary tree
# has the following definition:
#
# Populate each next pointer to point to its next right node. If
# there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space
# does not count as extra space for this problem.
#

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """

from collections import deque


class Solution:
    def connect(self, root):
        if not root:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            num = len(queue)

            for i in range(num):
                node = queue.popleft()
                if i + 1 == num:
                    node.next = None
                else:
                    nextNode = queue[0]
                    node.next = nextNode

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

    def connect2(self, root):
        if not root:
            return None

        leftMost = root

        while leftMost.left:

            node = leftMost

            while node:

                node.left.next = node.right

                if node.next:
                    node.right.next = node.next.left

                node = node.next

            leftMost = leftMost.left

        return root