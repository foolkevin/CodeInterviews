class Solution:
    def maxValue(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        for c in range(1, n):
            grid[0][c] += grid[0][c - 1]
        for r in range(1, m):
            grid[r][0] += grid[r - 1][0]
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += max(grid[r][c - 1], grid[r - 1][c])
        return grid[-1][-1]

if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    maxV = solution.maxValue(grid)
