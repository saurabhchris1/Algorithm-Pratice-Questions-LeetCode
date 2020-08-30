# Given two words (beginWord and endWord), and a dictionary's word list, find the
# length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        L = len(beginWord)
        wordDict = collections.defaultdict(list)

        for word in wordList:
            for i in range(L):
                wordDict[word[:i] + "*" + word[i + 1:]].append(word)

        visited = set()
        queue = collections.deque()
        queue.append((1, beginWord))

        while queue:
            level, currentWord = queue.popleft()

            for i in range(L):

                intermediateWord = currentWord[:i] + "*" + currentWord[i + 1:]

                for word in wordDict[intermediateWord]:

                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((level + 1, word))
        return 0
