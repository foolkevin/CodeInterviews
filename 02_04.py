class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        start, end, pos = None, None, head
        while pos is not None:
            newnode = ListNode(pos.val)
            if start is None:
                start = newnode
                end = start
            elif pos.val < x:
                newnode.next = start
                start = newnode
            else:
                end.next = newnode
                end = newnode
            pos = pos.next
        return start