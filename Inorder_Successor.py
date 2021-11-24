# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than p.val.
#
# Input: root = [2, 1, 3], p = 1
# Output: 2
# Explanation: 1
# 's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
#
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    class Solution:
        def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

            self.successor = None
            self.prev = None

            if p.right:
                curr = p.right
                while curr.left:
                    curr = curr.left
                self.successor = curr

            else:
                self.inorder_iterative(root, p)

            return self.successor

        def inorder_iterative(self, node, p):

            stack = []
            curr = node

            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()

                if self.prev == p:
                    self.successor = curr
                    return

                self.prev = curr
                curr = curr.right

        def inorder_recursive(self, node, p):

            if not node:
                return

            self.inorder(node.left, p)

            if self.prev == p and not self.successor:
                self.successor = node
                return

            self.prev = node

            self.inorder(node.right, p)
