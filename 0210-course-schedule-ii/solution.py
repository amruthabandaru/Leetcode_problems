from collections import defaultdict, deque
class Solution:
    def findOrder(self, n, prerequisites):
        graph = defaultdict(list)
        indeg = [0]*n
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        q = deque([i for i in range(n) if indeg[i] == 0])
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0: q.append(nxt)
        return res if len(res) == n else []

