class Solution:
    def countDigitOne(self, n: int) -> int:
        res, digit, low = 0, 1, 0
        while n > 0:
            high, curr = divmod(n, 10)
            n = high
            if curr == 0: res += high * digit
            elif curr == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += digit * curr
            digit *= 10
        return res


if __name__ == "__main__":
    n = 2314
    solution = Solution()
    res = solution.countDigitOne(n)