# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
#
# Input: "aba"
# Output: True
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.


class Solution:
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        skip = 0

        while left < right:
            if s[left] != s[right]:
                try1 = s[:left] + s[left + 1:]
                try2 = s[:right] + s[right + 1:]
                return try1 == try1[::-1] or try2 == try2[::-1]

            left += 1
            right -= 1
        return True
