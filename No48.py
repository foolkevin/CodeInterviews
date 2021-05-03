# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:19:42 2021

@author: Lenovo
"""

class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
               matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], \
                   matrix[j][n-1-i]= matrix[n-1-j][i], matrix[n-1-i][n-1-j], \
                   matrix[j][n-1-i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], 
              [13, 3, 6, 7], [15, 14, 12, 16]]
    solution = Solution()
    solution.rotate(matrix)
    