# Given a string s containing only lowercase English letters and the '?' character, convert all the '?'
# characters into lowercase letters such that the final string does not contain any consecutive repeating
# characters. You cannot modify the non '?' characters.
#
# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
#
# Return the final string after all the conversions (possibly zero) have been made. If there is more
# than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
#
# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions
# for this problem.From "azs" to "yzs", all are valid.Only "z" is an invalid modification as the string
# will consist of consecutive repeating characters in "zzs".
#
# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions
# for this problem.Only "v" and "w" are invalid modifications as the strings will consist of consecutive
# repeating characters in "ubvvw" and "ubvww".

class Solution:
    def modifyString(self, s: str) -> str:
        arr = list(s)

        for i in range(len(arr)):

            if arr[i] == "?":

                choice1 = choice2 = 0

                if i - 1 >= 0:
                    choice1 = ord(arr[i - 1])
                if i + 1 < len(arr):
                    choice2 = ord(arr[i + 1])

                val = 97
                while val == choice1 or val == choice2:
                    val += 1

                arr[i] = chr(val)

        return "".join(arr)