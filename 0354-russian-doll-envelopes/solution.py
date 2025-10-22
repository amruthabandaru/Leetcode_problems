class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        import bisect
        dp = []
        for _, h in envelopes:
            i = bisect.bisect_left(dp, h)
            if i == len(dp): dp.append(h)
            else: dp[i] = h
        return len(dp)

