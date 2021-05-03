class Solution:
    def majorityElement(self, nums) -> int:
        n, counter = len(nums), dict()
        if n == 1:
            return nums[0]
        for num in nums:
            if num in counter:
                counter[num] += 1
                if counter[num] > n / 2:
                    return num
            else:
                counter[num] = 1
        raise RuntimeError("The input array doesn't conform with specific assumption.")
            

if __name__ == "__main__":
    nums = [1]
    solution = Solution()
    num = solution.majorityElement(nums)