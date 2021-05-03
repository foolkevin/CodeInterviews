class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        prev, curr = head, head.next
        while curr and curr.val != val:
            prev, curr = curr, curr.next
        if curr:
            prev.next = curr.next
        return head