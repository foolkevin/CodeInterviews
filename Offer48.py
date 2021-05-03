class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        charDict, maxLen = dict(), 0
        recorder1, recorder2 = 0, 0
        for i, c in enumerate(s):
            lastPos = charDict.get(c, -1)
            charDict[c] = i
            recorder2 = recorder1 + 1 if i - lastPos > recorder1 else i - lastPos
            if recorder2 > maxLen: maxLen = recorder2
            recorder1 = recorder2
        return maxLen


if __name__ == "__main__":
    s = "pwwkew"
    solution = Solution()
    maxLen = solution.lengthOfLongestSubstring(s)
    
