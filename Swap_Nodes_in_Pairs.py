# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def swapPairs1(self, head):
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head

    def swapPairs2(self, head):

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummy.next
