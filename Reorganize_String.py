# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
#
# Return any possible rearrangement of s or return "" if not possible.
#
# Input: s = "aab"
# Output: "aba"
# Example 2:
#
# Input: s = "aaab"
# Output: ""

import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        dict = collections.Counter(s)
        heap = []
        for k, v in dict.items():
            heapq.heappush(heap, (-v, k))

        result = []
        while heap:
            count, char = heapq.heappop(heap)

            if len(result) > 0 and result[-1] == char:
                if not heap:
                    return ""
                tmpCnt, tmpChar = count, char
                count, char = heapq.heappop(heap)
                heapq.heappush(heap, (tmpCnt, tmpChar))

            result.append(char)
            count += 1
            if count:
                heapq.heappush(heap, (count, char))

        return "".join(result)