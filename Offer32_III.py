from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        nodeVal, nodeQueue = [], deque()
        nodeQueue.append(root)
        while nodeQueue:
            n, level = len(nodeQueue), []
            for _ in range(n):
                front = nodeQueue.popleft()
                if front.left:
                    nodeQueue.append(front.left)
                if front.right:
                    nodeQueue.append(front.right)
                level.append(front.val)
            nodeVal.append(level[::-1] if len(nodeVal) & 1 else level)
        return nodeVal
