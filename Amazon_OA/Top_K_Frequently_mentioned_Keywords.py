# Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords
# in order of most to least frequently mentioned.
#
# The comparison of strings is case-insensitive.
# Multiple occurances of a keyword in a review should be considred as a single mention.
# If keywords are mentioned an equal number of times in reviews, sort alphabetically.
#
# Example 1:
#
# Input:
# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#   "Anacell provides the best services in the city",
#   "betacellular has awesome services",
#   "Best services provided by anacell, everyone should use anacell",
# ]
#
# Output:
# ["anacell", "betacellular"]
#
# Explanation:
# "anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
# Example 2:
#
# Input:
# k = 2
# keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
# reviews = [
#   "I love anacell Best services; Best services provided by anacell",
#   "betacellular has great services",
#   "deltacellular provides much better services than betacellular",
#   "cetracular is worse than anacell",
#   "Betacellular is better than deltacellular.",
# ]
#
# Output:
# ["betacellular", "anacell"]
#
# Explanation:
# "betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews,
# but "anacell" is lexicographically smaller.

import collections
import heapq
import re


class Solution:

    def top_k(self, keywords, reviews, k):

        keywords_freq = collections.Counter()
        keywords_set = set(keywords)

        for review in reviews:
            review_words = set(review.lower().split(' '))

            review_words_temp = collections.defaultdict(int)
            for word in review_words:

                word = re.sub('[^a-z]', '', word)

                if word in keywords_set:
                    keywords_freq[word] += 1

        print (keywords_freq)

        heap = [(-freq, word) for word, freq in keywords_freq.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    keywords = ["anacell", "cetracular", "betacellular"]
    reviews = [
        "Anacell provides the best services in the city",
        "betacellular has awesome services",
        "Best services provided by anacell, everyone should use anacell",
    ]

    print(Solution().top_k(keywords, reviews, 2))

    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
        "I love anacell Best services; Best services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is better than deltacellular.",
    ]

    print(Solution().top_k(keywords, reviews, 2))
