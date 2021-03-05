# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        klist = lists[0]

        for i in range(1, len(lists)):
            klist = self.mergeTwoLlist(klist, lists[i])

        return klist

    # Divide and Conquer O(N log(k))
    def mergeKLists2(self, lists):
        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])

            interval *= 2

        return lists[0] if amount > 0 else None

    def mergeTwoLlist(self, l1, l2):
        list1 = l1
        list2 = l2
        head = ListNode(0)
        newList = head

        while list1 and list2:

            if list1.val <= list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next

            newList = newList.next

        if list1:
            newList.next = list1
        elif list2:
            newList.next = list2

        return head.next
