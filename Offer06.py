class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def reversePrint(self, head: ListNode):
        result = []
        if head == None:
            return result
        pos = head
        while pos is not None:
            result.append(pos.val)
            pos = pos.next
        result.reverse()
        return result
        