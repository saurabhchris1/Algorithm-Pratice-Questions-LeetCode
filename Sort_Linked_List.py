# Given the head of a linked list, return the list after sorting it in ascending order.
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        mid.next, mid = None, mid.next
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, list1, list2):
        l1 = list1
        l2 = list2
        newNode = ListNode(0)
        curr = newNode

        while l1 and l2:

            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return newNode.next

    def findMid(self, node):
        slow = node
        fast = node.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow