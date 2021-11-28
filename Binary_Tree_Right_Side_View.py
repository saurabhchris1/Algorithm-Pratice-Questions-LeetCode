# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
# Input: root = [1,null,3]
# Output: [1,3]
#
# Input: root = []
# Output: []

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def rightSideViewIterative(self, root):

        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            num = len(queue)

            for i in range(num):
                node = queue.popleft()
                if i == num - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return res

    def rightSideViewRecursive(self, root):

        if not root:
            return None

        self.res = []

        def helper(node, level):

            if not node:
                return

            if level == len(self.res):
                self.res.append(node.val)

            if node.right:
                helper(node.right, level + 1)

            if node.left:
                helper(node.left, level + 1)

        helper(root, 0)
        return self.res