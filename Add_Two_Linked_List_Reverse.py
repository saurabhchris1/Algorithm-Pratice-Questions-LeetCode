# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoNumbersHelper(l1, l2, 0)

    def addTwoNumbersHelper(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbersHelper(l1.next, l2.next, c)
        elif c:
            ret.next = ListNode(c)
        return ret


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    ans = Solution().addTwoNumbers(l1, l2)
    print(ans.next.next.val)
    print(ans.next.val)
    print(ans.val)
