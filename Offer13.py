def bitsum(a):
    sum = 0
    while a > 0:
        sum += a % 10
        a = a // 10
    return sum

class Solution:
    def __init__(self):
        self.total = 0
        self.record = None

    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0 or m <= 0 or n <= 0:
            return 0
        self.record = [False, ] * (m * n)
        self.movingCountCore(m, n, k, 0, 0)
        return self.total
        
    def movingCountCore(self, m: int, n: int, k: int, row: int, column: int) -> None:
        if (row < 0 or row >= m or column < 0 or column >= n or 
            self.record[row * n + column] or bitsum(row) + bitsum(column) > k):
            return
        self.total += 1
        self.record[row * n + column] = True
        self.movingCountCore(m, n, k, row, column + 1)
        self.movingCountCore(m, n, k, row + 1, column)