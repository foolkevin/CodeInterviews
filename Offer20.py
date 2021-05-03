class Solution:
    def isNumber(self, s: str) -> bool:
        state = [{' ': 0, 's': 1, 'd': 2, '.': 4}, 
                 {'d': 2, '.': 4},
                 {'d': 2, '.': 3, 'e': 5, ' ': 8},
                 {'d': 3, 'e': 5, ' ': 8}, 
                 {'d': 3}, 
                 {'s': 6, 'd': 7}, 
                 {'d': 7}, 
                 {'d': 7, ' ': 8}, 
                 {' ': 8}]
        p = 0
        for c in s:
            if '0' <= c <= '9': 
                t = 'd'
            elif c in '+-': 
                t = 's'
            elif c in 'Ee': 
                t = 'e'
            elif c in '. ':
                t = c
            else:
                t = '?'
            if t not in state[p]:
                return False
            p = state[p][t]
        return p in (2, 3 ,7, 8)
    
    def isNumberV2(self, s: str) -> bool:
        s = s.strip(' ')
        pos, length = 0, len(s)
    
        def integerSearch(s: str) -> bool:
            nonlocal pos
            length = len(s)
            if pos < length and s[pos] in "+-":
                pos += 1
            if not unsignedIntegerSearch(s):
                return False
            return True
        def unsignedIntegerSearch(s: str) -> bool:
            nonlocal pos
            start, length = pos, len(s)
            while pos < length and s[pos] >= '0' and s[pos] <= '9':
                pos += 1
            return pos > start 
        sign1, sign2 = integerSearch(s), False
        if pos < length and s[pos] == '.':
            pos += 1
            sign2 = unsignedIntegerSearch(s)
            if not sign1 and not sign2:
                return False
        if pos < length and (sign1 or sign2) and s[pos] in 'Ee':
            pos += 1
            if not integerSearch(s):
                return False
        return pos >= length


if __name__ == "__main__":
    s = "."
    solution = Solution()
    flag = solution.isNumberV2(s)
        