class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        addition, head, end = 0, None, None
        while l1 is not None or l2 is not None or addition != 0:
            sum = addition
            if l1 is not None:
                sum += l1.val
            if l2 is not None:
                sum += l2.val
            curr = ListNode(sum % 10)
            if head is None:
                head = curr
                end = head
            else:
                end.next = curr
                end = curr
            addition = sum // 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return head
