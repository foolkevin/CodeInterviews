class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counters = dict()
        for i in s:
            if i in counters:
                counters[i] += 1
            else:
                counters[i] = 1
        odd_counter = 0
        for value in counters.values():
            if value % 2 == 1:
                odd_counter += 1
            if odd_counter > 1:
                return False
        return True
