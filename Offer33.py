class Solution:
    def verifyPostorderV1(self, postorder) -> bool:
        def recur(postorder, start, end) -> bool:
            if start >= end: 
                return True
            i = end - 1
            while i >= start and postorder[i] > postorder[end]: 
                i -= 1
            middle = i
            while i >= start and postorder[i] < postorder[end]: 
                i -= 1
            return i < start and recur(postorder, start, middle) and\
                recur(postorder, middle + 1, end - 1)
        return recur(postorder, 0, len(postorder) - 1)
    
    def verifyPostorderV2(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True


if __name__ == "__main__":
    postorder = [1, 3, 2, 8, 10, 5]
    solution = Solution()
    isPostOrder = solution.verifyPostorderV2(postorder)
