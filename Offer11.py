class Solution:
    def minArray(self, numbers) -> int:
        low, high = 0, len(numbers) - 1
        if numbers[low] < numbers[high]:
            return numbers[low]
        while low < high:
            middle = (low + high) // 2
            if numbers[middle] < numbers[low]:
                high = middle
            elif numbers[middle] > numbers[high]:
                low = middle + 1
            else:
                high -= 1
        return numbers[low]
                