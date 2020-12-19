# Similar to three sum try to implement 4 sum

import collections


class Solution:
    def fourNumberSum(array, targetSum):
        seen = collections.defaultdict(list)
        res = []

        for i in range(1, len(array) - 1):

            for j in range(i + 1, len(array)):
                current = array[i] + array[j]
                diff = targetSum - current

                if diff in seen:

                    for pair in seen[diff]:
                        res.append([array[i], array[j]] + pair)

            for k in range(0, i):
                sums = array[k] + array[i]
                seen[sums].append([array[i], array[k]])

        return res
