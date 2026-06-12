class Solution:
    MOD = 10**9 + 7

    def dfs(self, u, parent, graph):
        self.up[u][0] = parent

        for j in range(1, self.LOG):
            self.up[u][j] = self.up[
                self.up[u][j - 1]
            ][j - 1]

        for v in graph[u]:
            if v == parent:
                continue

            self.depth[v] = self.depth[u] + 1
            self.dfs(v, u, graph)

    def lca(self, a, b):

        if self.depth[a] < self.depth[b]:
            a, b = b, a

        diff = self.depth[a] - self.depth[b]

        for j in range(self.LOG - 1, -1, -1):
            if diff & (1 << j):
                a = self.up[a][j]

        if a == b:
            return a

        for j in range(self.LOG - 1, -1, -1):
            if self.up[a][j] != self.up[b][j]:
                a = self.up[a][j]
                b = self.up[b][j]

        return self.up[a][0]

    def assignEdgeWeights(self, edges, queries):

        n = len(edges) + 1

        self.LOG = 20

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.up = [[0] * self.LOG for _ in range(n + 1)]
        self.depth = [0] * (n + 1)

        self.dfs(1, 1, graph)

        pow2 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % self.MOD

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            ancestor = self.lca(u, v)

            dist = (
                self.depth[u]
                + self.depth[v]
                - 2 * self.depth[ancestor]
            )

            ans.append(pow2[dist - 1])

        return ans