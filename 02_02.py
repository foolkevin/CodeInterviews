class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        kthNode, _ = self.kthNodeToLast(head, k)
        return kthNode.val

    def kthNodeToLast(self, head: ListNode, k: int) -> (ListNode, int):
        if head.next is None:
            return head, 1
        node, index = self.kthNodeToLast(head.next, k)
        index += 1
        if (index == k):
            return head, index
        return node, index
    
    def kthToLastInter(self, head: ListNode, k: int) -> int:
        predecessor, successor = head, head
        for _ in range(k):
            predecessor = predecessor.next
        while predecessor is not None:
            predecessor = predecessor.next
            successor = successor.next
        return successor.val