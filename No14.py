class Solution:
    def longestCommonPrefix(self, strs) -> str:
        length = len(strs)
        if length == 0:
            return ""
        if length == 1:
            return strs[0]
        commonprefix = ""
        for n in range(200):
            if n >= len(strs[0]):
                return commonprefix
            c = strs[0][n]
            for i in range(length):
                if n >= len(strs[i]) or strs[i][n] != c:
                    return commonprefix
            commonprefix = "".join([commonprefix, c])
        return commonprefix
    

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    solution = Solution()
    commonprefix = solution.longestCommonPrefix(strs)