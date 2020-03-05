# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
#
# Example 1:
#
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:
#
# Input: "aeiou"
# Output: ""


class Solution:
    def removeVowels(self, S):
        dict = {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'}
        res = []

        for c in S:
            if c not in dict:
                res.append(c)

        return "".join(res)
