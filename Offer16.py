def Pow(x: float, n: int) -> float:
    result = 1
    while n > 0:
        if n & 1:
            result *= x
        x *= x
        n = n >> 1
    return result

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x != 0 and n >= 0:
            return Pow(x, n)
        elif x != 0 and n < 0:
            return 1 / Pow(x, -n)
        elif x == 0 and n > 0:
            return 0
        elif x == 0 and n == 0:
            return 1
        else:
            raise ZeroDivisionError
