# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
# bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and
# no vertex has an edge to itself.
#
# You want to determine if there is a valid path that exists from vertex start to vertex end.
#
# Given edges and the integers n, start, and end, return true if there is a valid path from start to end,
# or false otherwise.
#
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
#
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges, start: int, end: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        return self.dfs(start, graph, end, visited)

    def dfs(self, node, graph, end, visited):
        if node == end:
            return True

        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph[node]:
            if self.dfs(neighbor, graph, end, visited):
                return True

    def bfs(self, n: int, edges, start: int, end: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()

        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node == end:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False