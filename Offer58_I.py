class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        i, res = len(s) - 1, []
        while i >= 0:
            j = i
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            if i > 0:
                res.append(' ')
                while s[i] == ' ':
                    i -= 1
        return ''.join(res)


if __name__ == "__main__":
    s = "the sky is blue"
    solution = Solution()
    res = solution.reverseWords(s)
        