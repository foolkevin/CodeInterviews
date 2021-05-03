class Solution:
    def strToInt(self, string: str) -> int:
        string = string.strip()
        if not string: return 0
        int_max, int_min, boundary = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        num, i, sign = 0, 1, 1
        if string[0] == '-': sign = -1
        elif string[0] != '+': i = 0
        for s in string[i:]:
            if not '0' <= s <= '9': break
            if num > boundary or num == boundary and s > '7':
                return int_max if sign == 1 else int_min
            num = num * 10 + ord(s) - ord('0')
        return num * sign


if __name__ == "__main__":
    solution = Solution()
    testStr = "-91283472332"
    num = solution.strToInt(testStr)
    print(num)
