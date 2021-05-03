class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, n = 0, 0, len(nums)
        while r < n:
            if nums[r] != 0:
                if r > l:
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    solution.moveZeroes(nums)