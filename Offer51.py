class Solution:
    def reversePairs(self, nums) -> int:
        def mergeSort(nums, start, end, result, counter) -> int:
            def merge(nums, start, end, result, counter) -> int:
                endLeft = (start + end) >> 1
                indexLeft, indexRight = start, endLeft + 1
                for index in range(start, end + 1):
                    if indexLeft > endLeft:
                        result[index] = nums[indexRight]
                        indexRight += 1
                    elif indexRight > end or nums[indexLeft] <= nums[indexRight]:
                        result[index] = nums[indexLeft]
                        indexLeft += 1
                    else:
                        result[index] = nums[indexRight]
                        indexRight += 1
                        counter += endLeft - indexLeft + 1
                return counter
                
            if start >= end:
                return counter
            middle = (start + end) >> 1
            counter = mergeSort(nums, start, middle, result, counter)
            counter = mergeSort(nums, middle + 1, end, result, counter)
            counter = merge(nums, start, end, result, counter)
            nums[start:end + 1] = result[start:end + 1]
            return counter
        result = [0] * len(nums)
        counter = 0
        return mergeSort(nums, 0, len(nums) - 1, result, counter)