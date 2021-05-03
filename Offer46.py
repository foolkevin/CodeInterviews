class Solution:
    def translateNum(self, num: int) -> int:
        digits = []
        if 0 <= num < 10: return 1
        while num > 0:
            digits.append(num % 10)
            num //= 10
        recorder1= 1
        recorder2 = 2 if 10 <= digits[-1] * 10 + digits[-2] < 26 else 1
        for i in range(len(digits) - 3, -1, -1):
            recorder2, recorder1 = recorder2 + recorder1 if 10 <= digits[i + 1] * 10 \
                + digits[i] < 26 else recorder2, recorder2
        return recorder2


if __name__ == "__main__":
    num = 0
    solution = Solution()
    counts = solution.translateNum(num)