class Solution:
    def compressString(self, S: str) -> str:
        compressed = []
        n = len(S)
        if n <= 1:
            return S
        count = 0
        for i in range(n):
            count += 1
            if i + 1 >= n or S[i] != S[i + 1]:
                compressed.append(S[i])
                compressed.append(str(count))
                count = 0
        return "".join(compressed) if len(compressed) < n else S
