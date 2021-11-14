# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside
# the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white
# spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example
# 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example
# 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example
# 4:
#
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"


class Solution:
    def decodeString(self, s):
        stack = []

        for i in range(len(s)):
            char = s[i]

            if char == ']':

                res = []
                while stack[-1] != '[':
                    res.append(stack.pop())

                stack.pop()
                base = 1
                k = 0
                while stack and stack[-1].isdigit():
                    k += base * int(stack.pop())
                    base *= 10

                while k != 0:
                    for char in res[::-1]:
                        stack.append(char)
                    k -= 1

            else:
                stack.append(char)

        return "".join(stack)