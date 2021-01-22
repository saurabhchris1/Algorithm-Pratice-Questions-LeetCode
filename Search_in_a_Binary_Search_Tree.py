# Search in a Binary Search Tree
# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return
# the subtree rooted with that node. If such a node does not exist, return null.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root

        while curr:
            currVal = curr.val

            if val > currVal:
                curr = curr.right
            elif val < currVal:
                curr = curr.left
            else:
                return curr

        return None