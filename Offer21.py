class Solution:
    def exchange(self, nums):
        pointer1, pointer2, n = 0, 0, len(nums)
        while pointer1 < n and pointer2 < n:
            while (nums[pointer2] & 1 == 0 or pointer2 <= pointer1):
                pointer2 += 1
                if (pointer2 >= n):
                    return nums
            while (pointer1 < n and nums[pointer1] & 1 == 1):
                pointer1 += 1
            if (pointer1 >= pointer2):
                continue
            nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
            pointer1 += 1
            pointer2 += 1
        return nums
    def exchangeV2(self, nums):
        return sorted(nums, key=lambda x: x % 2, reverse=True)
    def exchangeV3(self, nums):
        pointer1, pointer2 = 0, len(nums) - 1
        while pointer1 < pointer2:
            while pointer1 < pointer2 and nums[pointer1] & 1 == 1:
                pointer1 += 1
            while pointer1 < pointer2 and nums[pointer2] & 1 == 0:
                pointer2 -= 1
            nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
        return nums


if __name__ == "__main__":
    nums = [1, 3, 2, 5, 4, 6]
    solution = Solution()
    nums = solution.exchange(nums)
        