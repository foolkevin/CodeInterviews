# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:05:47 2021

@author: Lenovo
"""
class Solution:
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result_intervals = []
        for interval in sorted_intervals:
            if not result_intervals or result_intervals[-1][1] < interval[0]:
                result_intervals.append(interval)
            else:
                result_intervals[-1] = [result_intervals[-1][0], 
                                        max(result_intervals[-1][1], 
                                            interval[1])]
        return result_intervals