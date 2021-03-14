# A linked list of length n is given such that each node contains an
# additional random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of
# exactly n brand new nodes, where each new node has its value set to the
# value of its corresponding original node. Both the next and random pointer
# of the new nodes should point to new nodes in the copied list such that the
# pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list,
# where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]

        return None
    # Time: O(n) Space: O(n)
    def copyRandomList(self, head):
        if not head:
            return head

        old_node = head
        new_node = Node(old_node.val, None, None)

        self.visited[old_node] = new_node

        while old_node:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

    # Time: O(n) Space: O(1)
    def copyRandomListOptimized(self, head: 'Node') -> 'Node':
        if not head:
            return head

        current = head
        while current:
            newNode = Node(current.val, None, None)

            newNode.next = current.next
            current.next = newNode
            current = newNode.next

        current = head
        while current:
            current.next.random = current.random.next if current.random else None
            current = current.next.next

        old = head
        new = head.next
        newHead = new
        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next else None

            old = old.next
            new = new.next

        return newHead