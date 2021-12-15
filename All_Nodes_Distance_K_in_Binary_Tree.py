# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the
# values of all nodes that have a distance k from the target node.

#
# You can return the answer in any order.
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
#
# Input: root = [1], target = 1, k = 3
# Output: []

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from  collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        parents = {}

        def dfs(node, parent):
            parents[node] = parent

            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)

        dfs(root, None)

        queue = deque([(target, 0)])
        res = []
        seen = set()
        while queue:
            level = len(queue)

            for _ in range(level):

                node, distance = queue.popleft()
                seen.add(node)
                if distance == k:
                    res.append(node.val)

                for nextNode in [node.left, node.right, parents[node]]:
                    if nextNode and nextNode not in seen:
                        queue.append((nextNode, distance + 1))
        return res
