# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
# possible paths from node 0 to node n - 1 and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit from
# node i (i.e., there is a directed edge from node i to node graph[i][j]).
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#
# Input: graph = [[1],[]]
# Output: [[0,1]]
#
# Input: graph = [[1,2,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,2,3],[0,3]]
#
# Input: graph = [[1,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,3]]

from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph):

        res = []
        self.findPaths(0, graph, [], res)
        return res

    def findPaths(self, node, graph, path, res):
        path.append(node)
        if node == len(graph) - 1:
            res.append(list(path))
            return

        for neighbor in graph[node]:
            self.findPaths(neighbor, graph, path, res)
            path.pop()

    def findPathsBFS(self, graph):
        end = len(graph) - 1
        start = 0
        queue = deque([(start, [start])])

        res = []
        while queue:
            node, currPath = queue.popleft()

            if node == end:
                res.append(currPath)

            for neighbor in graph[node]:
                queue.append((neighbor, currPath + [neighbor]))
        return res