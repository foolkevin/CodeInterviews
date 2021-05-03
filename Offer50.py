from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> str:
        keyDict = OrderedDict()
        for char in s:
            if char in keyDict:
                keyDict[char] = False
            else:
                keyDict[char] = True
        for char, counts in keyDict.items():
            if counts == 1:
                return char
        return " "