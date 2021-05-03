class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, pos = head, head
        for _ in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            pos, fast = pos.next, fast.next
        return pos
        