# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


class Solution:
    # Brute Force 2^n Time and O(n) Space
    def wordBreak(self, s, wordDict):

        # if not s:
        #     return True
        #
        # for word in wordDict:
        #
        #     if s[0:len(word)] == word and self.wordBreak(s[len(word):], wordDict):
        #         return True
        #
        # return False

        memo = {}

        return self.helper(s, wordDict, memo)

    def helper(self, s, wordDict, memo):

        if not s:
            return True
        elif s in memo:
            return memo[s]

        for word in wordDict:

            if s[0:len(word)] == word and self.helper(s[len(word):], wordDict, memo):
                memo[s] = True
                return True

        memo[s] = False
        return False

    # Using Memo O(n^2) Time and O(n) Space
