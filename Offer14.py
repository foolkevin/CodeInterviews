def remainder(x, a, p):
    result = 1
    for _ in range(a):
        result = (result * x) % p
    return result

class Solution:
    def cuttingRope(self, n: int) -> int:
        record = [0, ] * (n + 1)
        record[1] = 1
        for i in range(2, n + 1):
            multiplymax = 1
            for j in range(1, i // 2 + 1):
                multiplymax = max([record[j] * record[i - j], j * record[i - j], 
                                  j * (i - j), multiplymax])
            record[i] = multiplymax
        return record[-1]
    
    def cuttingRopeGreedy(self, n: int) -> int:
        record = [0, 1, 1, 2]
        if n <= 3:
            return record[n]
        num, remain, p = n // 3, n % 3, 1000000007
        if remain == 1:
            return (remainder(3, num - 1, p) * 4) % p
        elif remain == 0:
            return remainder(3, num, p)
        else:
            return (remainder(3, num, p) * 2) % p


if __name__ == "__main__":
    n = 8
    solution = Solution()
    result = solution.cuttingRope(n)