# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):

        curr = head
        newListTail = None
        newListHead = None

        while curr:
            count = 0
            curr = head

            while count < k and curr:
                curr = curr.next
                count += 1

            if count == k:
                revHead = self.reverse(head, k)

                if not newListHead:
                    newListHead = revHead

                if newListTail:
                    newListTail.next = revHead

                newListTail = head
                head = curr

        if newListTail:
            newListTail.next = head

        return newListHead if newListHead else head

    def reverse(self, l, k):

        curr = l
        temp = None
        prev = None

        while k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1

        return prev
