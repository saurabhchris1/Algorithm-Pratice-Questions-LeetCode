# Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.
#
# Return the minimum cost of deletions such that there are no two identical letters next to each other.
#
# Notice that you will delete the chosen characters at the same time, in other words, after deleting a character,
# the costs of deleting other characters will not change.
#
# Input: s = "abaac", cost = [1,2,3,4,5]
# Output: 3
# Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other)
#
# Input: s = "abc", cost = [1, 2, 3]
# Output: 0
# Explanation: You
# don
# 't need to delete any character because there are no identical letters next to each other.
#
# Input: s = "aabaa", cost = [1,2,3,4,1]
# Output: 2
# Explanation: Delete the first and the last character, getting the string ("aba").

class Solution:
    def minCost(self, s, cost):

        if len(s) < 2:
            return 0

        res = 0
        left = 0

        for right in range(1, len(s)):

            if s[left] == s[right]:
                res += min(cost[left], cost[right])

                if cost[left] < cost[right]:
                    left = right
            else:
                left = right

        return res