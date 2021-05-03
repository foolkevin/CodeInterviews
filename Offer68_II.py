class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        nodeLeft = self.lowestCommonAncestor(root.left, p, q)
        nodeRight = self.lowestCommonAncestor(root.right, p, q)
        if not nodeLeft: return nodeRight
        if not nodeRight: return nodeLeft
        return root