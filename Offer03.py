class Solution:
    def findRepeatNumber(self, nums) -> int:
        record = set()
        for i in nums:
            if i in record:
                return i
            record.add(i)
        return 0