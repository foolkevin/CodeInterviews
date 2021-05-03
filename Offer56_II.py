class Solution:
    def singleNumber(self, nums) -> int:
        ones = twos = 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


if __name__ == "__main__":
    nums = [3, 4, 3, 3]
    solution = Solution()
    result = solution.singleNumber(nums)