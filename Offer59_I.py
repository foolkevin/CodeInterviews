from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        windowQueue, res = deque(), []
        if not nums: return []
        n = len(nums)
        for i in range(k):
            while windowQueue and windowQueue[-1] < nums[i]:
                windowQueue.pop()
            windowQueue.append(nums[i])
        for i in range(n - k + 1):
            res.append(windowQueue[0])
            if windowQueue[0] == nums[i]: windowQueue.popleft()
            if i < n - k:
                while windowQueue and i < n - k and windowQueue[-1] < nums[i + k]:
                    windowQueue.pop()
                windowQueue.append(nums[i + k])
        return res


if __name__ == "__main__":
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    solution = Solution()
    results = solution.maxSlidingWindow(nums, k)