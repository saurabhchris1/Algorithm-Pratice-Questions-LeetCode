
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    stack = []
    curr = tree
    count = 0

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.right

        curr = stack.pop()
        count += 1
        if count == k:
            return curr.value
        curr = curr.left

    return None