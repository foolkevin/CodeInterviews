import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int):
        result, path = [], []
        def recurV1(node: TreeNode, rem, tempList):
            prefix = tempList.copy()
            if not node.left and not node.right:
                if rem == node.val:
                    prefix.append(node.val)
                    result.append(prefix)
                    del prefix
                return
            prefix.append(node.val)
            if node.left:
                recurV1(node.left, rem - node.val, prefix)
            if node.right:
                recurV1(node.right, rem - node.val, prefix)
        
        def recurV2(node, rem):
            if not node: return
            path.append(node.val)
            rem -= node.val
            if rem == 0 and not node.left and not node.right:
                result.append(path.copy())
            recurV2(root.left, rem)
            recurV2(root.right, rem)
            path.pop()
            
        # if root:
        #     recurV1(root, target, path)
        recurV2(root, target)
        return result

def buildTree(treeNodeList):
    n = len(treeNodeList)
    for i in range(n // 2):
        if not treeNodeList[i]:
            continue
        treeNodeList[i].left = treeNodeList[2 * i + 1]
        treeNodeList[i].right = treeNodeList[2 * i + 2]
    return treeNodeList[0]


if __name__ == '__main__':
    # treeListStr = input("Please enter in a complete binary tree: ")
    # treeNodeList = [TreeNode(val=int(item)) if item != 'null' else None 
    #                 for item in treeListStr.split(' ') ]
    treeValList = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    treeNodeList = [TreeNode(val=item) if item else None for item in treeValList]
    root = buildTree(treeNodeList)
    solution = Solution()
    target = 22
    result = solution.pathSum(root, target)