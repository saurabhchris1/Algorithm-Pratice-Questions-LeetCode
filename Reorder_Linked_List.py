# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        second = prev
        first = head

        while second.next:
            temp1 = first.next
            first.next = second
            temp2 = second.next
            second.next = temp1
            first = temp1
            second = temp2