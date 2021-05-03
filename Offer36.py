class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        def dfs(node: Node):
            if not node.left and not node.right:
                node.left = node
                node.right = node
                return node, node
            head, end, temp = node, node, node.right
            temp = node.right
            if node.left:
                leftHead, leftEnd = dfs(node.left)
                leftEnd.right, node.left = node, leftEnd
                leftHead.left, node.right = node, leftHead
                head = leftHead
            if temp:
                rightHead, rightEnd = dfs(temp)
                node.right, rightHead.left = rightHead, node
                head.left, rightEnd.right = rightEnd, head
                end = rightEnd
            return head, end
        if not root: return root
        head, _ = dfs(root)
        return head


if __name__ == "__main__":
    valList = [1, 2, 3, 4, 5]
    nodeList = [Node(val) for val in valList]
    nodeList[3].left, nodeList[3].right = nodeList[1], nodeList[4]
    nodeList[1].left, nodeList[1].right = nodeList[0], nodeList[2]
    solution = Solution()
    head = solution.treeToDoublyList(nodeList[3])