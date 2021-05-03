class Solution:
    def numWays(self, n: int) -> int:
        reg = [1, 1, 2]
        if n <= 2:
            return reg[n]
        f1, f2 = 1, 2
        for _ in range(2, n):
            f2, f1 = f1 + f2, f2
        return f2 % 1000000007