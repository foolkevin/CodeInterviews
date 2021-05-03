# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:22:43 2021

@author: Lenovo
"""
from collections import Counter
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        if len(counter2) != len(counter2):
            return False
        for key in counter1:
            if key not in counter2 or counter1[key] != counter2[key]:
                return False
        return True


if __name__ == '__main__':
    s1 = 'a'    
    s2 = 'ab'
    solution = Solution()
    print(solution.CheckPermutation(s1, s2))