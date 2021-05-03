class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepthV1(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepthV1(root.left), self.maxDepthV1(root.right)) + 1
    
    def maxDepthV2(self, root: TreeNode) -> int:
        if not root: return 0
        queueCurr, queueNext, depth = [root], [], 0
        while queueCurr:
            while queueCurr:
                node = queueCurr.pop()
                if node.left: queueNext.append(node.left)
                if node.right: queueNext.append(node.right)
            queueCurr, queueNext = queueNext, []
            depth += 1
        return depth
