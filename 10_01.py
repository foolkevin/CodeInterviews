class Solution:
    def merge(self, A, m: int, B, n: int) -> None:
        if len(A) != m + n:
            raise ValueError("A.length != n + m")
        if n == 0: return A 
        pointerA, pointerB, pointerSet = m - 1, n - 1, m + n - 1
        while pointerA >= 0 and pointerB >= 0:
            if A[pointerA] >= B[pointerB]:
                A[pointerSet] = A[pointerA]
                pointerA -= 1
            else:
                A[pointerSet] = B[pointerB]
                pointerB -= 1
            pointerSet -= 1
        if pointerB >= 0:
            A[:pointerB + 1] = B[:pointerB + 1]