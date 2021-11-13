# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

import collections
class Solution:
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        dict_t = collections.Counter(t)
        formed = 0
        ans = float("inf"), None, None
        window_count = collections.defaultdict(int)
        l, r = 0, 0
        required = len(dict_t)

        while r < len(s):

            char = s[r]
            window_count[char] += 1

            if char in dict_t and window_count[char] == dict_t[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                char = s[l]
                window_count[char] -= 1
                if char in dict_t and window_count[char] < dict_t[char]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]