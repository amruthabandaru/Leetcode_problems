from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        res, q, left_to_right = [], deque([root]), True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
        return res

