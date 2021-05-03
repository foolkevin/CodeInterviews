import functools

class Solution:
    def minNumber(self, nums) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0

        strNums = [str(num) for num in nums]
        strNums.sort(key=functools.cmp_to_key(sort_rule))
        return "".join(strNums)


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    solution = Solution()
    minNumber = solution.minNumber(nums)
        
