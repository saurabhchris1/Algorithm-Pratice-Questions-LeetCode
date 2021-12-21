# A peak element is an element that is strictly greater than its neighbors.
#
# Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# You must write an algorithm that runs in O(log n) time.

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
# or index number 5 where the peak element is 6.

class Solution:
    def findPeakElement(self, nums) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low) // 2

            n1 = 0
            n2 = 0

            if mid - 1 < 0:
                n1 = float("-inf")
            else:
                n1 = nums[mid - 1]

            if mid + 1 == len(nums):
                n2 = float("-inf")
            else:
                n2 = nums[mid + 1]

            if nums[mid] < n1:
                high = mid - 1
            elif nums[mid] < n2:
                low = mid + 1
            else:
                return mid

        return -1