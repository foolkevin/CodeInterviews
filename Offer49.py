class Solution:
    def nthUglyNumber(self, n: int) -> int:
        record = [1]
        a = b = c = 0
        for i in range(1, n):
            record.append(min(record[a]*2, record[b]*3, record[c]*5))
            while record[a] * 2 <= record[-1]: a += 1
            while record[b] * 3 <= record[-1]: b += 1
            while record[c] * 5 <= record[-1]: c += 1
        return record[-1]


if __name__ == "__main__":
    n = 10
    solution = Solution()
    uglyNumber = solution.nthUglyNumber(n)