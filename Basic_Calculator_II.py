# Given a string s which represents an expression, evaluate this expression and return its value.
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
# Input: s = "3+2*2"
# Output: 7
#
# Input: s = " 3/2 "
# Output: 1
#
# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s):

        if not s:
            return 0

        stack = []
        currNum = 0
        operation = '+'
        operators = {'+', '-', '*', '/'}
        nums = set(str(x) for x in range(10))

        for i in range(len(s)):
            currChar = s[i]

            if currChar in nums:
                currNum = currNum * 10 + int(currChar)

            if currChar in operators or i == len(s) - 1:

                if operation == '+':
                    stack.append(currNum)

                elif operation == '-':
                    stack.append(-currNum)

                elif operation == '*':
                    stack[-1] *= currNum

                elif operation == '/':
                    stack[-1] = int(stack[-1] / currNum)

                operation = currChar
                currNum = 0

        return sum(stack)