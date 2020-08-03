# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().
#


class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        pattern = self.buildPattern(needle)
        return self.findIndex(haystack, needle, pattern)

    def buildPattern(self, needle):
        pattern = [-1 for i in needle]
        j, i = 0, 1

        while i < len(needle):
            if needle[i] == needle[j]:
                pattern[i] = j
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1

        return pattern

    def findIndex(self, haystack, needle, pattern):
        i, j = 0, 0
        while i < len(haystack):

            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return i - j
                i += 1
                j += 1

            elif j > 0:
                j = pattern[j - 1] + 1

            else:
                i += 1

        return -1
