class Solution:
    def search(self, nums, target: int) -> int:
        def rightBoundary(target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = (left + right) >> 1
                if nums[middle] <= target:
                    left = middle + 1
                else:
                    right = middle - 1
            return left
        return rightBoundary(target) - rightBoundary(target - 1)


if __name__ == "__main__":
    nums = [1]
    solution = Solution()
    count = solution.search(nums, 1)
