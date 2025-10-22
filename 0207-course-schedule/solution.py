from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indeg = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        visited = 0
        while q:
            cur = q.popleft()
            visited += 1
            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return visited == numCourses

