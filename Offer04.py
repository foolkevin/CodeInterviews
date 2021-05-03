class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        n = len(matrix)
        if n <= 0:
            return False
        x, y = 0, len(matrix[0]) - 1
        while x <= n - 1 and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False