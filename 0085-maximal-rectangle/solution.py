class Solution:
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        heights = [0]*m
        res = 0
        for row in matrix:
            for i in range(m):
                heights[i] = heights[i]+1 if row[i] == '1' else 0
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights):
        stack, res = [], 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1] - 1
                res = max(res, H * W)
            stack.append(i)
        return res

