from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(preorder) != len(inorder) or len(preorder) == 0:
            return None
        hashtable = {x: i for i, x in enumerate(inorder)}
        return self.buildTreeRecursion(preorder, inorder, 0, len(preorder) - 1, 
                                       0, len(inorder) - 1, hashtable)

    def buildTreeRecursion(self, preorder, inorder, prestart, preend, 
                           instart, inend, hashtable):
        if preend < prestart:
            return None
        elif preend == prestart:
            return TreeNode(preorder[prestart])
        else:
            root = TreeNode(preorder[prestart])
            length = hashtable[preorder[prestart]] - instart
            root.left = self.buildTreeRecursion(preorder, inorder, prestart + 1, 
                                                prestart + length, instart, 
                                                instart + length - 1, hashtable)
            root.right = self.buildTreeRecursion(preorder, inorder, 
                                                 prestart + length + 1, 
                                                 preend, instart + length + 1, 
                                                 inend, hashtable)
            return root
    
    def buildTreeIter(self, preorder, inorder):
        inorderIndex = 0
        nodeStack = deque()
        root = TreeNode(preorder[0])
        nodeStack.append(root)
        for i in range(1, len(preorder)):
            if nodeStack[-1].val != inorder[inorderIndex]:
                nodeStack[-1].left = TreeNode(preorder[i])
                nodeStack.append(nodeStack[-1].left)
            else:
                while len(nodeStack) > 0 and nodeStack[-1].val == inorder[inorderIndex]:
                    topnode = nodeStack.pop()
                    inorderIndex += 1
                topnode.right = TreeNode(preorder[i])
                nodeStack.append(topnode.right)
        return root

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    tree = solution.buildTree(preorder, inorder)