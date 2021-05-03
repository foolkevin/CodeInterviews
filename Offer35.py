class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head: return
        nodeDict = dict()
        cur = head
        while cur:
            nodeDict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            nodeDict[cur].next = nodeDict.get(cur.next)
            nodeDict[cur].random = nodeDict.get(cur.random)
            cur = cur.next
        return nodeDict[head]

    def copyRandomListV2(self, head: Node) -> Node:
        if not head: return
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = node.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        new = post = head.next
        while post.next:
            cur.next = cur.next.next
            post.next = post.next.next
            cur = cur.next
            post = post.next
        cur.next = None
        post.next = None
        return new

        