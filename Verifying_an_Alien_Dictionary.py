# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some permutation
# of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted lexicographicaly
# in this alien language.
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
# hence the sequence is unsorted.
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter
# (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where
# '∅' is defined as the blank character which is less than any other character (More info).


class Solution:
    def isAlienSorted(self, words, order):
        dict = {}

        for idx, char in enumerate(order):
            dict[char] = idx

        for i in range(len(words) - 1):

            for j in range(len(words[i])):

                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if dict[words[i][j]] > dict[words[i + 1][j]]:
                        return False

                    break

        return True