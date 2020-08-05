# Given a paragraph and a list of banned words, return the most frequent word that
# is not in the list of banned words.  It is guaranteed there is at least one word
# that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.
# Words in the paragraph are not case sensitive.  The answer is in lowercase.
#
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned
# word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
#
# Note:
#
# 1 <= paragraph.length <= 1000.
# 0 <= banned.length <= 100.
# 1 <= banned[i].length <= 10.
# The answer is unique, and written in lowercase (even if its occurrences in paragraph
# may have uppercase symbols, and even if it is a proper noun.)
# paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
# There are no hyphens or hyphenated words.
# Words only consist of letters, never apostrophes or other punctuation symbols.

import collections


class Solution:
    def mostCommonWord(self, paragraph, banned):
        # paraSet = {"!", "?", "'", ",", ";", "."}
        # normal = []
        # # O(n) Time and O(n) space
        # for char in paragraph:
        #     if char in paraSet:
        #         normal.append(' ')
        #
        #     else:
        #         normal.append(char.lower())
        # # O(N)
        # normal = ''.join(normal)
        # words = normal.split()
        # O(M)
        # banned = set(banned)
        # word_dict = collections.defaultdict(int)
        #
        # for word in words:
        #     if word in banned:
        #         continue
        #     word_dict[word] += 1
        #
        # res = ""
        # num = 0
        #
        # for key, val in word_dict.items():
        #
        #     if val > num:
        #         num = val
        #         res = key
        #
        # return res

        banned = set(banned)
        word_dict = collections.defaultdict(int)
        buffer = []
        maxSize = 0
        ans = ''

        for i, char in enumerate(paragraph):

            if char.isalnum():
                buffer.append(char.lower())
                if i < len(paragraph) - 1:
                    continue

            if len(buffer) > 0:
                word = ''.join(buffer)
                if word not in banned:
                    word_dict[word] += 1

                    if word_dict[word] > maxSize:
                        maxSize = word_dict[word]
                        ans = word

                buffer = []

        return ans
