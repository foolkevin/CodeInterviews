class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            digit += 1
            start *= 10
            count = 9 * digit * start
        num = start + (n - 1) // digit
        nthDigit = int(str(num)[(n - 1) % digit])
        return nthDigit


if __name__ == "__main__":
    n = 11
    solution = Solution()
    digit = solution.findNthDigit(n)