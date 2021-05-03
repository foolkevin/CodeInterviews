class Solution:
    def permutation(self, s: str):
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append("".join(c))
                return
            charSet = set()
            for i in range(x, len(c)):
                if c[i] in charSet: continue
                charSet.add(c[i])
                c[x], c[i] = c[i], c[x]
                dfs(x + 1)
                c[x], c[i] = c[i], c[x]
        
        dfs(0)
        return res
