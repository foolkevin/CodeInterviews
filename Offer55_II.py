class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root) -> int:
            if not root:
                return 0
            leftHeight = recur(root.left)
            if leftHeight == -1: return -1
            rightHeight = recur(root.right)
            if rightHeight == -1: return -1
            if abs(leftHeight - rightHeight) <= 1:
                return max(leftHeight, rightHeight) + 1
            else:
                return -1
        return recur(root) != -1