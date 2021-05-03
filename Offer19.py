class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        state = [[False, ] * n for _ in range(m)]
        state[0][0] = True
        for j in range(2, n, 2):
            state[0][j] = state[0][j - 2] and p[j - 1] == '*'
        for i in range(1, m):
            for j in range(1, n):
                state[i][j] = state[i][j - 2] or state[i - 1][j] and \
                    (s[i - 1] == p[j - 2] or p[j - 2] == '.') if p[j - 1] == '*' else \
                        state[i - 1][j - 1] and (s[i - 1] == p[j - 1] or \
                            p[j - 1] == '.')
        return state[-1][-1]