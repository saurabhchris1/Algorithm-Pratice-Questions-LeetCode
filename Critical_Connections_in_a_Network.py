# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where
# connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly
# or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
#
# Return all critical connections in the network in any order.
#
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

import collections


class Solution:
    rank = {}
    graph = collections.defaultdict(list)
    connDict = {}

    def criticalConnections(self, n, connections):
        self.formGraph(n, connections)
        self.dfs(0, 0)

        res = []
        for node in self.connDict:
            res.append(node)

        return res

    def dfs(self, node, discoveryRank):

        if self.rank[node]:
            return self.rank[node]

        self.rank[node] = discoveryRank

        minRank = discoveryRank + 1

        for neighbor in self.graph[node]:

            if self.rank[neighbor] and self.rank[neighbor] == discoveryRank - 1:
                continue

            recurrsiveRank = self.dfs(neighbor, discoveryRank + 1)

            if recurrsiveRank <= discoveryRank:
                del self.connDict[(min(neighbor, node), max(neighbor, node))]

            minRank = min(minRank, recurrsiveRank)

        return minRank

    def formGraph(self, n, connections):
        self.rank = {}
        self.graph = collections.defaultdict(list)
        self.connDict = {}

        for node in range(n):
            self.rank[node] = None

        for connection in connections:
            u = connection[0]
            v = connection[1]

            self.graph[u].append(v)
            self.graph[v].append(u)

            self.connDict[(min(u, v), max(u, v))] = 1