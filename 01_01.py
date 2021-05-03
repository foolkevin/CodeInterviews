# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:56:46 2021

@author: Lenovo
"""

class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for s in astr:
            bit = ord(s) - ord('a')
            if mark & (1 << bit):
                return False
            mark |= (1 << bit)
        return True