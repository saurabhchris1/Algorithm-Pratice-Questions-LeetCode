# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
# so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()

        for idx, char in enumerate(s):

            if char not in "()":
                continue
            elif char == "(":
                stack.append(idx)
            elif not stack:
                remove.add(idx)
            else:
                stack.pop()

        if stack:
            for i in stack:
                remove.add(i)
        res = []

        for idx, char in enumerate(s):

            if idx not in remove:
                res.append(char)

        return "".join(res)