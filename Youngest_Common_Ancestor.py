# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
# two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a
# node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according
# to the LCA definition.


class Solution:

    def youngest(self, node, p, q):

        if not node:
            return None

        if node == p or node == q:
            return node

        left = self.youngest(node.left, p, q)
        right = self.youngest(node.right, p, q)

        if not left:
            return right

        if not right:
            return left

        return node

    def iterative(self, root, p, q):

        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:

            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parent[node.left] = node

            if node.right:
                stack.append(node.right)
                parent[node.right] = node

        ancestor = set()

        while p:
            ancestor.add(p)
            p = parent[p]

        while q not in ancestor:
            q = parent[q]

        return q
