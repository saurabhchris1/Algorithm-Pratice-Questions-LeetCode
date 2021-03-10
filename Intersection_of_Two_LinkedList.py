# Write a program to find the node at which the intersection of two singly linked lists begins.

# intersection of two Linked list

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next

        return pA


if __name__ == "__main__":
    arr1 = [4, 1]
    arr2 = [5, 0, 1]
    arr3 = [8, 4, 5]
    node1 = ListNode(arr1[0])
    node2 = ListNode(arr2[0])
    node3 = ListNode(arr3[0])
    n1 = node1
    n2 = node2
    n3 = node3

    for i in arr3[1:]:
        n3.next = ListNode(i)
        n3 = n3.next
    for i in arr1[1:]:
        n1.next = ListNode(i)
        n1 = n1.next
    n1.next = node3

    for i in arr2[1:]:
        n2.next = ListNode(i)
        n2 = n2.next
    n2.next = node3
    finalnode = Solution().getIntersectionNode(node1, node2)
    print(finalnode, finalnode.val)
