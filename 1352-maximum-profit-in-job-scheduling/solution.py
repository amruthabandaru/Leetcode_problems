import bisect
class Solution:
    def jobScheduling(self, start, end, profit):
        jobs = sorted(zip(end, start, profit))
        dp = [(0, 0)]
        for e, s, p in jobs:
            i = bisect.bisect(dp, (s, float('inf'))) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append((e, dp[i][1] + p))
        return dp[-1][1]

