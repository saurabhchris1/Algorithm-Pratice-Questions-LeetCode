# Given an input string , reverse the string word by word.
#
# Example:
#
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note:
#
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# Follow up: Could you do it in-place without allocating extra space?


class Solution:
    def reverseWords(self, s):

        self.reverse(s, 0, len(s) - 1)
        self.reverse_each_word(s)

    def reverse(self, l, left, right):

        while left <= right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l):
        n = len(l)
        start = end = 0

        while start < n:

            while end < n and l[end] != " ":
                end += 1

            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1
