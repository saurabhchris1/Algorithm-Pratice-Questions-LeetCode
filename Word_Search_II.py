# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
# are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

class Node:
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord
        self.wordKey = None


class Solution:
    def __init__(self):
        self.trie = Node({}, False)

    def findWords(self, board, words):
        current = None
        for word in words:
            current = self.trie
            for char in word:
                if char not in current.children:
                    current.children[char] = Node({}, False)
                current = current.children[char]
            current.isWord = True
            current.wordKey = word
        res = set()
        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] in self.trie.children:
                    self.backtrack(board, row, col, self.trie, res)
        return res

    def backtrack(self, board, row, col, parent, res):
        letter = board[row][col]
        node = parent.children[letter]

        if node.isWord:
            res.add(node.wordKey)

        board[row][col] = "#"

        for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newRow = row + r
            newCol = col + c

            if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]):
                if board[newRow][newCol] in node.children:
                    self.backtrack(board, newRow, newCol, node, res)

        board[row][col] = letter
        if not node.children:
            del parent.children[letter]