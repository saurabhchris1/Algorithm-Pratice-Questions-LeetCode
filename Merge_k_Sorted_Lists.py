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
        if not lists:
            return None

        return self.mergeSort(lists, 0, len(lists) - 1)

    def mergeSort(self, lists, start, end):

        if start == end:
            return lists[start]

        mid = start + (end - start) // 2

        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)

        return self.merge(left, right)

    def merge(self, list1, list2):
        l1 = list1
        l2 = list2
        newList = ListNode(0)
        curr = newList

        while l1 and l2:

            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2

        return newList.next
