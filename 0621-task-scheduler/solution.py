from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        count = list(Counter(tasks).values())
        maxc = max(count)
        idle = (maxc - 1) * (n + 1)
        return max(len(tasks), idle + count.count(maxc))

