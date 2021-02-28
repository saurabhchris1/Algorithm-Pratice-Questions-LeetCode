# Design a class which receives a list of words in the constructor,
# and implements a method that takes two words word1 and word2 and return
# the shortest distance between these two words in the list. Your method will
# be called repeatedly many times with different parameters.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1

import collections


class WordDistance:

    def __init__(self, words):
        self.locations = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.locations[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:

        loc1 = self.locations[word1]
        loc2 = self.locations[word2]
        l1 = 0
        l2 = 0
        minDistance = float("inf")

        while l1 < len(loc1) and l2 < len(loc2):

            minDistance = min(abs(loc1[l1] - loc2[l2]), minDistance)

            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1

        return minDistance