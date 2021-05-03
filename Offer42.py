class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        if n < 1:
            raise ValueError("The length must not be lower than 1.") 
        maxTail = [nums[0]] * len(nums)
        for i in range(1, n):
            maxTail[i] = max(maxTail[i - 1] + nums[i], nums[i])
        return max(maxTail)