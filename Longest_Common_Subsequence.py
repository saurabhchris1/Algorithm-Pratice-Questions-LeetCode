# Given two strings text1 and text2, return the length of
# their longest common subsequence.
#
# A subsequence of a string is a new string generated from
# the original string with some characters(can be none) deleted
# without changing the relative order of the remaining characters.
# (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common
# subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.


class Solution:
    def longestCommonSubsequence(self, text1, text2):

        grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):

                if text2[col] == text1[row]:
                    grid[row][col] = 1 + grid[row + 1][col + 1]
                else:
                    grid[row][col] = max(grid[row + 1][col], grid[row][col + 1])

        return grid[0][0]