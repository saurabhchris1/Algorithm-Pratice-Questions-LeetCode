# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:
#
# Input: 1
# Output: "A"
# Example 2:
#
# Input: 28
# Output: "AB"
# Example 3:
#
# Input: 701
# Output: "ZY"


class Solution:
    def convertToTitle(self, n):
        res = []

        while columnNumber > 0:
            right = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            res.append(chr(65 + right % 26))

        return "".join(res[::-1])
