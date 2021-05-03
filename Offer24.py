class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prevNode = None
        while head.next:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        head.next = prevNode
        return head