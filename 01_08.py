class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow, ncolumn = len(matrix), len(matrix[0])
        rowrecord, colunmrecord = [0, ] * nrow, [0, ] * ncolumn
        for i in range(nrow):
            for j in range(ncolumn):
                if matrix[i][j] == 0:
                    rowrecord[i] = 1
                    colunmrecord[j] = 1
        for i in range(nrow):
            for j in range(ncolumn):
                if rowrecord[i] == 1 or colunmrecord[j] == 1:
                    matrix[i][j] = 0
            
