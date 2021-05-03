class Solution:
    def __init__(self):
        self.row, self.columns = 0, 0
        self.wordlen = 0
        self.record = None
        self.index = 0

    def exist(self, board, word) -> bool:
        if len(board) == 0 or len(word) == 0:
            return False
        self.index = 0
        self.rows, self.columns = len(board), len(board[0])
        self.wordlen = len(word)
        if self.wordlen > self.rows * self.columns:
            return False
        self.record = [False, ] * (self.rows * self.columns)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.hasPathElements(board, i, j, word):
                    return True
        return False
    
    def hasPathElements(self, board, row, column, word):
        if self.index == self.wordlen:
            return True
        if (row < 0 or row >= self.rows or column < 0 or column >= self.columns
            or self.record[row * self.columns + column] or 
            board[row][column] != word[self.index]):
            return False
        self.index += 1
        self.record[row * self.columns + column] = True
        hasPath = (self.hasPathElements(board, row, column - 1, word) or 
                   self.hasPathElements(board, row, column + 1, word) or 
                   self.hasPathElements(board, row - 1, column, word) or 
                   self.hasPathElements(board, row + 1, column, word))
        if not hasPath:
            self.index -= 1
            self.record[row * self.columns + column] = False
            return False
        return hasPath


if __name__ == "__main__":
    board = [["a", "b"], ["c", "d"]]
    word = "acdb"
    solution = Solution()
    solution.exist(board, word)