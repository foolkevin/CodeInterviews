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
            front = nodeQueue.popleft()
            if front.left:
                nodeQueue.append(front.left)
            if front.right:
                nodeQueue.append(front.right)
            nodeVal.append(front.val)
        return nodeVal

