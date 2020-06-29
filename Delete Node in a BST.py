# Given a root node reference of a BST and a key, delete the node with the given key
# in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root, key):
        return self.remove(root, key)

    def remove(self, node, value, parent=None):
        current = node

        while current:
            if value > current.val:
                parent = current
                current = current.right
            elif value < current.val:
                parent = current
                current = current.left

            else:
                if current.left and current.right:
                    current.val = self.getMin(current.right)
                    self.remove(current.right, current.val, current)
                elif parent is None:
                    if current.left:
                        current.val = current.left.val
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right:
                        current.val = current.right.val
                        current.left = current.right.left
                        current.right = current.right.right

                    else:
                        return None
                        break

                elif parent.left == current:
                    parent.left = current.left if current.left else current.right
                elif parent.right == current:
                    parent.right = current.left if current.left else current.right

                break

        return node

    def getMin(self, node):

        current = node
        while current.left:
            current = current.left

        return current.val
