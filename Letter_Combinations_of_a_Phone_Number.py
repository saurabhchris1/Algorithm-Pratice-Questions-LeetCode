# Given a string containing digits from 2-9 inclusive, return
# all possible letter combinations that the number could represent.
# Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.
# phone = {
#     '2': ['a', 'b', 'c'],
#     '3': ['d', 'e', 'f'],
#     '4': ['g', 'h', 'i'],
#     '5': ['j', 'k', 'l'],
#     '6': ['m', 'n', 'o'],
#     '7': ['p', 'q', 'r', 's'],
#     '8': ['t', 'u', 'v'],
#     '9': ['w', 'x', 'y', 'z']
# }
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]


class Solution:
    def letterCombinations(self, digits):
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(combination, nextDigits):
            if len(nextDigits) == 0:
                res.append(combination)
            else:
                for char in phone[nextDigits[0]]:
                    backtrack(combination + char, nextDigits[1:])

        res = []
        if digits:
            backtrack("", digits)
        return res
