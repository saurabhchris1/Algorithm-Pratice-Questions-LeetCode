# Given an array of size n, find the majority element. The majority
# element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2

import collections


class Solution:
    # O(n) Time and O(n) space
    def majorityElement(self, nums):
        count = 0
        res = 0

        for num in nums:
            if count == 0:
                res = num

            count += 1 if num == res else -1

        return res
