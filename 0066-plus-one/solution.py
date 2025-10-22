class Solution:
    def plusOne(self, digits):
        n = int(''.join(map(str, digits))) + 1
        return [int(i) for i in str(n)]

