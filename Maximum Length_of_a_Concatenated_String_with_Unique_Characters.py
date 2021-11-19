# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:
#
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:
#
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
# Example 4:
#
# Input: arr = ["aa","bb"]
# Output: 0
# Explanation: Both strings in arr do not have unique characters, thus there are no valid concatenations.


from collections import Counter
class Solution:
    def maxLength(self, arr):

        return self.backtrack(arr, 0, Counter())

    def backtrack(self, arr, pos, res_map):

        if res_map:
            if max(res_map.values()) > 1:
                return 0

        best = len(res_map)

        for i in range(pos, len(arr)):

            word_map = Counter(arr[i])
            if len(word_map) != len(arr[i]):
                continue

            res_map.update(word_map)
            best = max(best, self.backtrack(arr, i + 1, res_map))

            for c in word_map:
                if res_map[c] == word_map[c]:
                    del res_map[c]
                else:
                    res_map[c] -= 1

        return best