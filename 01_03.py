# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:59:10 2021

@author: Lenovo
"""

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")