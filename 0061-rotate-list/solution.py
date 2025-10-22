class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head
        k = k % length
        for _ in range(length - k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head

