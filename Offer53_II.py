class Solution:
    def missingNumber(self, nums) -> int:
        length = len(nums)
        if nums[0] > 0: return 0
        if nums[-1] < length: return length
        left, right = 0, length - 1
        while left <= right:
            middle = (left + right) >> 1
            if nums[middle] == middle:
                left = middle + 1
            else:
                right = middle - 1
        return left
        