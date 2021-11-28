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

        while left <= right:

            if s[left] != s[right]:
                try1 = self.isValid(s, left + 1, right)
                try2 = self.isValid(s, left, right - 1)

                return try1 or try2

            left += 1
            right -= 1

        return True

    def isValid(self, word, left, right):

        while left <= right:

            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
