class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def recur(L: TreeNode, R: TreeNode):
            if not L and not R:
                return True
            elif L and R and L.val == R.val:
                return recur(L.left, R.right) and recur(L.right, R.left)
            else:
                return False
        return recur(root.left, root.right)