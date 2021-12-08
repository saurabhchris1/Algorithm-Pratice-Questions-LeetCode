# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y,
# return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
#
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:

        parent = {root: None}
        seen = {}
        stack = [(root, 0)]
        while x not in seen or y not in seen:
            node, depth = stack.pop()

            seen[node.val] = (node, depth)
            if node.left:
                parent[node.left] = node
                stack.append((node.left, depth + 1))

            if node.right:
                parent[node.right] = node
                stack.append((node.right, depth + 1))

        nodeX, depthX = seen[x]
        nodeY, depthY = seen[y]
        if parent[nodeX] == parent[nodeY]:
            return False
        return depthX == depthY