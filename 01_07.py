# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 23:14:00 2021

@author: Lenovo
"""

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = [0, 0]
        end = [1, len(matrix) - 1]
        step = end[1]
        while step > 0:
            # rotate from outside to inside layer by layer
            self.rotate_border(matrix, start, end, step)
            start = [start[0]+1, start[1]+1]
            end = [end[0]+1, end[1]-1]
            step -= 2
            
    def rotate_border(self, matrix, start, end, step):
        row, column = start
        if step > 1:
            orders = [('row+1', step+1), ('column+1', step), 
                      ('row-1', step-1)]
        elif step == 1:
            orders = [('row+1', 2), ('column+1', 1)]
        for i, (order, order_step) in enumerate(orders):     
            for j in range(order_step):
                if (i > 0 or j > 0) and order[:-2] == 'row':
                    row = eval(order)
                if (i > 0 or j > 0) and order[:-2] == 'column':
                    column = eval(order)
                pointer = [row, column]
                for k in range(step):
                    if pointer[0] == start[0]:
                        matrix[pointer[0]][pointer[1]], matrix[pointer[0]][pointer[1]+1] = \
                        matrix[pointer[0]][pointer[1]+1], matrix[pointer[0]][pointer[1]]
                        pointer[1] += 1
                        continue
                    if pointer[1] == start[1]:
                        matrix[pointer[0]][pointer[1]], matrix[pointer[0]-1][pointer[1]] = \
                        matrix[pointer[0]-1][pointer[1]], matrix[pointer[0]][pointer[1]]
                        pointer[0] -= 1
                        continue
                    if pointer[0] == end[1]:
                        matrix[pointer[0]][pointer[1]], matrix[pointer[0]][pointer[1]-1] = \
                        matrix[pointer[0]][pointer[1]-1], matrix[pointer[0]][pointer[1]]
                        pointer[1] -= 1
                        continue
                    if pointer[1] == end[1]:
                        matrix[pointer[0]][pointer[1]], matrix[pointer[0]+1][pointer[1]] = \
                        matrix[pointer[0]+1][pointer[1]], matrix[pointer[0]][pointer[1]]
                        pointer[0] += 1
                        continue


if __name__ == "__main__":
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], 
              [13, 3, 6, 7], [15, 14, 12, 16]]
    solution = Solution()
    solution.rotate(matrix)