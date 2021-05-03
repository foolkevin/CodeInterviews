class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        result = []
        def spiralLayer(matrix, result, srow, erow, scolumn, ecolumn):
            if erow < srow or ecolumn < scolumn:
                return
            i, j = srow, scolumn
            if srow == erow:
                while j <= ecolumn:
                    result.append(matrix[i][j])
                    j += 1
                return
            if scolumn == ecolumn:
                while i <= erow:
                    result.append(matrix[i][j])
                    i += 1
                return
            while j < ecolumn:
                result.append(matrix[i][j])
                j += 1
            while i < erow:
                result.append(matrix[i][j])
                i += 1
            while j > scolumn:
                result.append(matrix[i][j])
                j -= 1
            while i > srow:
                result.append(matrix[i][j])
                i -= 1
            spiralLayer(matrix, result, srow + 1, erow - 1, scolumn + 1, ecolumn - 1)
        spiralLayer(matrix, result, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
        return result