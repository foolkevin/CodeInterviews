# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:40:53 2021

@author: Lenovo
"""
class Solution:
    def searchInsert(self, nums, target) -> int:
        right = len(nums) - 1
        left = 0
        if nums[0] >= target:
            return 0
        if nums[right] < target:
            return right + 1
        if nums[right] == target:
            return right
        while right - left > 1:  
            center = (right + left) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center
            else:
                right = center
        return right
