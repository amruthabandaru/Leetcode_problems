class Solution:
    def reverseKGroup(self, head, k):
        node = head
        for _ in range(k):
            if not node: return head
            node = node.next
        prev = self.reverseKGroup(node, k)
        for _ in range(k):
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

