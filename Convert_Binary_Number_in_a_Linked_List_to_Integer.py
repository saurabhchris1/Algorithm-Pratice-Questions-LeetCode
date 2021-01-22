# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1. The l
# inked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        power = -1
        node = head
        while node:
            node = node.next
            power += 1

        node = head
        res = 0
        while node:
            res += pow(2, power) * node.val
            power -= 1
            node = node.next

        return res