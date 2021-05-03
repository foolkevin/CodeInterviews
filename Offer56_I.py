class Solution:
    def singleNumbers(self, nums):
        m, z = 0, 1
        for num in nums:
            m ^= num
        while z & m == 0: z <<= 1
        x = y = 0
        for num in nums:
            if num & z: x ^= num
            else: y ^= num
        return x, y


if __name__ == "__main__":
    nums = [1, 2, 5, 2]
    solution = Solution()
    x, y = solution.singleNumbers(nums)
        