class Solution:
    def getLeastNumbersV1(self, arr, k: int):
        def quicksort(arr, l, r):
            if l >= r: return 
            base = arr[l]
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= base: j -= 1
                while i < j and arr[i] <= base: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            quicksort(arr, l, i - 1)
            quicksort(arr, i + 1, r)

        quicksort(arr, 0, len(arr) - 1)
        return arr[:k]

    def getLeastNumbersV2(self, arr, k: int):
        if k >= len(arr):
            return arr
        def quicksort(arr, l, r):
            base = arr[l]
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= base: j -= 1
                while i < j and arr[i] <= base: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                return quicksort(arr, l, i - 1)
            elif k > i + 1:
                return quicksort(arr, i + 1, r)
            else:
                return arr[:k]
        return quicksort(arr, 0, len(arr) - 1)