class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = int(str(x)[::-1])
        return sign * rev if rev < 2**31 else 0

