# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
#
# For
# simplicity, each
# node
# 's value is the same as the node'
# s
# index(1 - indexed).For
# example, the
# first
# node
# with val == 1, the second node with val == 2, and so on.The graph is represented in the
# test case using an adjacency list.An adjacency list is a collection of unordered lists used to
# represent a finite graph.Each list describes the set of neighbors of a node in the graph.The given
# node will always be the first node with val = 1. You must return the copy of the given node as a
# reference to the cloned graph.
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
#
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
#
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

class Solution:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clonedNode = Node(node.val, [])

        self.visited[node] = clonedNode

        if node.neighbors:
            clonedNode.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]

        return clonedNode

    def cloneGraphIterative(self, node: 'Node') -> 'Node':

        if not node:
            return node

        queue = deque([node])
        visited = {node: Node(node.val, [])}

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:

                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])

                    queue.append(neighbor)

                visited[n].neighbors.append(visited[neighbor])

        return visited[node]