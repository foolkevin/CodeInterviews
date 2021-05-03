class Solution:
    def validateStackSequences(self, pushed, poped) -> bool:
        i, j, n, m = 0, 0, len(pushed), len(poped)
        if n != m:
            return False
        if n == 0:
            return True
        stack = []
        while i < n:
            stack.append(pushed[i])
            while stack and stack[-1] == poped[j]:
                stack.pop()
                j += 1
            i += 1
        return not stack