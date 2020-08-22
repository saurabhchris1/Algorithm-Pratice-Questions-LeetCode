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

        res = 0
        sign = 1 if x > 0 else -1
        x *= sign

        while x:
            pop = x % 10
            res = res * 10 + pop
            if res > pow(2, 31) - 1 or res < -pow(2, 31):
                return 0
            x = x // 10

        res = res if sign > 0 else res * sign

        return res
