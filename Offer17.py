class Solution:
    def printNumbers(self, n: int) -> list:
        def dfs(x):
            if x == n:
                num = ''.join(nums[self.start:])
                if num != '0':
                    res.append(int(num))
                if n - self.start == self.nine:
                    self.start -= 1
                return
            else:
                for i in range(10):
                    if i == 9:
                        self.nine += 1
                    nums[x] = str(i)
                    dfs(x + 1)
                self.nine -= 1
        
        nums, res = ['0'] * n, []
        self.start = n - 1
        self.nine = 0
        dfs(0)
        return res


if __name__ == "__main__":
    n = 2
    solution = Solution()
    res = solution.printNumbers(n)