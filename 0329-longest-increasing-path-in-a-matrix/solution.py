class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        def dfs(r, c, prev):
            if not (0 <= r < rows and 0 <= c < cols) or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp: return dp[(r, c)]
            val = matrix[r][c]
            dp[(r, c)] = 1 + max(dfs(r+1,c,val), dfs(r-1,c,val), dfs(r,c+1,val), dfs(r,c-1,val))
            return dp[(r, c)]
        return max(dfs(r, c, -1) for r in range(rows) for c in range(cols))

