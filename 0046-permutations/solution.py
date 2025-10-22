class Solution:
    def permute(self, nums):
        res = []
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:]); return
            for n in nums:
                if n in used: continue
                used.add(n)
                path.append(n)
                backtrack(path, used)
                path.pop(); used.remove(n)
        backtrack([], set())
        return res

