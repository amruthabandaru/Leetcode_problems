class Solution:
    def verticalTraversal(self, root):
        nodes = []
        def dfs(node, r, c):
            if not node: return
            nodes.append((c, r, node.val))
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
        dfs(root, 0, 0)
        nodes.sort()
        res, last = [], None
        for c, r, v in nodes:
            if c != last:
                res.append([])
                last = c
            res[-1].append(v)
        return res

