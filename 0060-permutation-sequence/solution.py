class Solution:
    def getPermutation(self, n, k):
        from math import factorial
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        res = ''
        for i in range(n, 0, -1):
            idx = k // factorial(i - 1)
            res += nums.pop(idx)
            k %= factorial(i - 1)
        return res

