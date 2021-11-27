# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1, l2):
        n1 = self.findLength(l1)
        n2 = self.findLength(l2)

        head = None
        curr1 = l1
        curr2 = l2

        while n1 > 0 or n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1

            node = ListNode(val)
            node.next = head
            head = node

        carry = 0
        newHead = None

        while head:
            num = head.val + carry
            carry = num // 10
            node = ListNode(num % 10)
            head = head.next
            node.next = newHead
            newHead = node

        if carry:
            node = ListNode(carry)
            node.next = newHead
            newHead = node
        return newHead

    def findLength(self, ll):
        curr = ll
        n = 0
        while curr:
            n += 1
            curr = curr.next

        return n

    # def addTwoNumbers(self, l1, l2):
    #
    #     q1 = deque()
    #     q2 = deque()
    #
    #     while l1 or l2:
    #
    #         if l1 and l2:
    #             q1.append(l1.val)
    #             q2.append(l2.val)
    #             l1 = l1.next
    #             l2 = l2.next
    #         elif l1 and not l2:
    #             q1.append(l1.val)
    #             q2.appendleft(0)
    #             l1 = l1.next
    #         elif not l1 and l2:
    #             q1.appendleft(0)
    #             q2.append(l2.val)
    #             l2 = l2.next
    #
    #     carry = 0
    #     curr = None
    #
    #     while q1 and q2:
    #         num1 = q1.pop()
    #         num2 = q2.pop()
    #
    #         num = num1 + num2 + carry
    #         carry = num // 10
    #         node = ListNode(num % 10)
    #
    #         node.next = curr
    #         curr = node
    #
    #     if carry != 0:
    #         node = ListNode(carry)
    #         node.next = curr
    #         curr = node
    #
    #     return curr


if __name__ == "__main__":
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 8 -> 0 -> 7
    ans = Solution().addTwoNumbers(l1, l2)
    while ans:
        print(ans.val)
        ans = ans.next
