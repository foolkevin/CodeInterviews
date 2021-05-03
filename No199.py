from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftSideView(self, root: TreeNode):
        if not root: return []
        results, queue = [], deque()
        queue.append(root)
        while queue:
            register = []
            results.append(queue[0].val)
            while queue:
                node = queue.popleft()
                if node.left:
                    register.append(node.left)
                if node.right:
                    register.append(node.right)
            queue = deque(register)
        return results


if __name__ == "__main__":
    valList = [1, 2, 3, 5, 4]
    nodeList = [TreeNode(val=val) for val in valList]
    root = nodeList[0]
    root.left, root.right = nodeList[1], nodeList[2]
    nodeList[1].right, nodeList[2].right = nodeList[3], nodeList[4]
    solution = Solution()
    leftView = solution.leftSideView(root)