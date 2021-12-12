# Given an array nums, there is a sliding window of size k which is moving
# from the very left of the array to the very right. You can only see the k
# numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?

import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        left = 0
        right = 0
        queue = collections.deque()
        res = []

        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)

            if left > queue[0]:
                queue.popleft()

            if right + 1 >= k:
                res.append(nums[queue[0]])
                left += 1

            right += 1
        return res
