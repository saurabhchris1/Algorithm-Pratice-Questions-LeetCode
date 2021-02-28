# Given a list of words and two words word1 and word2, return
# the shortest distance between these two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1


class Solution:
    def shortestDistance(self, words, word1, word2):

        i1 = -1
        i2 = -1
        minDistance = len(words)

        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                minDistance = min(minDistance, abs(i2 - i1))

        return minDistance