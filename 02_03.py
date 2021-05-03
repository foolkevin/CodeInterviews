class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteNode(self, node):
        curr = node
        while curr.next.next is not None:
            curr.val = curr.next.val
            curr = curr.next
        curr.val = curr.next.val
        curr.next = None