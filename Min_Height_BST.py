# Min Height BST
# Given an array create the min height BST


def minHeightBst(array):
    return helper(0, len(array) - 1, None, array)


def helper(left, right, node, array):
    if left > right:
        return
    mid = left + (right - left) // 2
    if not node:
        node = BST(array[mid])
    else:
        node.insert(array[mid])

    helper(left, mid - 1, node, array)
    helper(mid + 1, right, node, array)

    return node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
