class Solution:
    def findContinuousSequence(self, target: int):
        i, j, sumVal, res = 1, 2, 3, []
        while i < j:
            if sumVal > target:
                sumVal -= i
                i += 1
            elif (sumVal < target):
                j += 1
                sumVal += j
            else:
                res.append(list(range(i, j + 1)))
                j += 1
                sumVal += j
        return res
