class Solution:
    def findDiagonalOrder(self, matrix):
        row = len(matrix)
        if row == 0:
            return []
        column = len(matrix[0])
        result = []
        flag, sign, max_iters, max_elements, elements = True, 1, \
            abs(row - column), min(row, column), 1
        row_id, column_id = 0, 0
        for _ in range(1, row + column):
            counter = 1
            while counter <= elements:
                result.append(matrix[row_id][column_id])
                row_id -= sign
                column_id += sign
                counter += 1
            if elements < max_elements and flag:
                elements += 1
            elif max_iters == 0:
                elements -= 1
                flag = False
            else:
                max_iters -= 1
            sign = -sign
            if row_id >= row:
                row_id -=1
                column_id += 2
            if column_id >= column:
                column_id -= 1
                row_id += 2
            if row_id < 0:
                row_id += 1
            if column_id < 0:
                column_id += 1
        return result


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    result = solution.findDiagonalOrder(matrix)