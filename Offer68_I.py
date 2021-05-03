class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        minVal, maxVal = min(p.val, q.val), max(p.val, q.val)
        pos = root
        while pos:
            if minVal > pos.val:
                pos = pos.right
            elif maxVal < pos.val:
                pos = pos.left
            else:
                break
        return pos
