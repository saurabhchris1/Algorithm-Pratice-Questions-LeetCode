# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false


class Solution:
    def exist(self, board, word):

        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True

    def backtrack(self, row, col, suffix):

        if len(suffix) == 0:
            return True

        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.board[row][col] != suffix[0]:
            return False

        self.board[row][col] = '#'

        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:

            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        self.board[row][col] = suffix[0]

        return False
