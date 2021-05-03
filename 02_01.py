class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        valset = set([head.val])
        pos = head
        while pos.next is not None:
            curr = pos.next
            if curr.val in valset:
                pos.next = curr.next
            else:
                valset.add(curr.val)
                pos = pos.next
        return head 