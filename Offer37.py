from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"
        reg, res = deque([root]), []
        while any(reg):
            node = reg.popleft()
            if node:
                res.append(str(node.val))
                reg.append(node.left)
                reg.append(node.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        valList = [int(char) if 'n' not in char else None for char in data[1:-1].split(',')]
        root, n = TreeNode(valList[0]), len(valList)
        reg, pointer = deque([root]), 1
        while reg:
            if pointer >= n: break
            node = reg.popleft()
            if valList[pointer] is not None:
                node.left = TreeNode(valList[pointer])
                reg.append(node.left)
            pointer += 1
            if pointer >= n: break
            if valList[pointer] is not None:
                node.right = TreeNode(valList[pointer])
                reg.append(node.right)
            pointer += 1
        return root


if __name__ == "__main__":
    valStr = "[-1, 0, 1]"
    codec = Codec()
    root = codec.deserialize(valStr)
    encodes = codec.serialize(root)
    print(encodes)