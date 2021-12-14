# Given a Binary Search Tree and a target number, return true if there exist two
# elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
# Example 2:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):

        dict = {}
        queue = collections.deque()
        queue.append(root)

        while queue:
            num = len(queue)
            for _ in range(num):
                node = queue.popleft()

                if k - node.val in dict:
                    return True
                dict[node.val] = 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False

    def findTargetInorder(self, root, k: int) -> bool:
        inorder = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right

        left = 0
        right = len(inorder) - 1

        while left < right:

            num = inorder[left] + inorder[right]

            if num > k:
                right -= 1
            elif num < k:
                left += 1
            else:
                return True
        return False
