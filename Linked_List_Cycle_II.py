# Given a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in
# the list that can be reached again by continuously following
# the next pointer. Internally, pos is used to denote the index
# of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Notice that you should not modify the linked list.
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        intersection = self.findIntersection(head)

        if not intersection:
            return None

        ptr1 = head
        ptr2 = intersection
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

    def findIntersection(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return fast

        return None