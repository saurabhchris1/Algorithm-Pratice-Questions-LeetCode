# A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
#
# Given three integers a, b and c, return any string s, which satisfies following conditions:
#
# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and
# at most c occurrences of the letter 'c'
# s will only contain 'a', 'b' and 'c' letters.
# If there is no such string s return the empty string "".
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
#
# Input: a = 2, b = 2, c = 1
# Output: "aabbc"
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It's the only correct answer in this case.

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if char[0]:
                heapq.heappush(heap, char)

        result = []
        while heap:
            count, char = heapq.heappop(heap)

            if len(result) > 1 and result[-1] == result[-2] == char:
                if not heap:
                    break
                tmpCnt, tmpChar = count, char
                count, char = heapq.heappop(heap)
                heapq.heappush(heap, (tmpCnt, tmpChar))

            result.append(char)
            count += 1
            if count:
                heapq.heappush(heap, (count, char))

        return "".join(result)