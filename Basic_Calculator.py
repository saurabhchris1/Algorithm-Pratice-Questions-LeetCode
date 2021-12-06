# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
# Input: s = "1 + 1"
# Output: 2
# Example 2:
#
# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
    def calculate(self, s):
        stack = []
        currNum = 0
        res = 0
        sign = 1

        for char in s:

            if char.isdigit():
                currNum = currNum * 10 + int(char)

            if char == "+":
                res += sign * currNum
                sign = 1
                currNum = 0
            elif char == "-":
                res += sign * currNum
                sign = -1
                currNum = 0
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif char == ")":
                res += sign * currNum
                res *= stack.pop()
                res += stack.pop()

                currNum = 0

        return res + sign * currNum