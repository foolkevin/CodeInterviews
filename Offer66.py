class Solution:
    def constructArr(self, a):
        n = len(a)
        if n == 0: return []
        b = [1] * n
        for i in range(1, n):
            b[i] *= b[i - 1] * a[i - 1]
        temp = a[n - 1]
        for j in range(n - 2, -1, -1):
            b[j] *= temp
            temp *= a[j]
        return b