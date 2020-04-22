# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21


class Solution:
    def reverse(x):

        num = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x = -1 * x

        while x // 10 > 0:
            right = x % 10

            num = num * 10 + right

            x = x // 10

        num = num * 10 + x

        if num < pow(-2, 31) or num > pow(2, 31) - 1:
            return 0

        if is_negative:
            return num * -1

        return num
