# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:18:07 2021

@author: Lenovo
"""
class Solution:
    def pivotIndex(self, nums) -> int:
        s0 = sum(nums)
        s1 = 0
        for i in range(len(nums)):
            if s1 == s0 - nums[i] - s1:
                return i
            s1 += nums[i]
        return -1
