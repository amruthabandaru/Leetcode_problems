class Solution:
    def generate(self, numRows):
        res = [[1]]
        for _ in range(1, numRows):
            prev = res[-1]
            row = [1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1]
            res.append(row)
        return res

