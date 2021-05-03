class Solution:
    def dicesProbability(self, n: int):
        p = 1 / 6
        results = [p, ] * 6
        for _ in range(n - 1):
            length = len(results)
            temp = results.copy()
            results = [0, ] * (length + 5)
            for i in range(length):
                results[i: i + 6] = [item + temp[i] * p \
                    for j, item in enumerate(results[i: i + 6])]
        return results


if __name__ == "__main__":
    n = 2
    solution = Solution()
    probability = solution.dicesProbability(n)