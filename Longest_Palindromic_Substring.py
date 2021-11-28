# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxVal = [0, (0, 0)]

        for i in range(len(s)):
            odd = self.maxValid(s, i, i)
            even = self.maxValid(s, i, i + 1)

            if even[1] - even[0] + 1 > maxVal[0]:
                maxVal[0] = even[1] - even[0] + 1
                maxVal[1] = (even[0], even[1])

            if odd[1] - odd[0] + 1 > maxVal[0]:
                maxVal[0] = odd[1] - odd[0] + 1
                maxVal[1] = (odd[0], odd[1])

        return s[maxVal[1][0]: maxVal[1][1] + 1]

    def maxValid(self, word, left, right):

        while left >= 0 and right < len(word):

            if word[left] != word[right]:
                break
            left -= 1
            right += 1

        left += 1
        right -= 1
        return left, right
