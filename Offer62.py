class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        num = 0
        for i in range(2, n + 1):
            num = (num + m) % i
        return num