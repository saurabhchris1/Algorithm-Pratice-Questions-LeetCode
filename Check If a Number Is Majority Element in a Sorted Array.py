# Given an array nums sorted in non-decreasing order, and a number target,
# return True if and only if target is a majority element.
#
# A majority element is an element that appears more than N/2 times in an array of length N.
#
# Example 1:
#
# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
# Output: true
# Explanation:
# The value 5 appears 5 times and the length of the array is 9.
# Thus, 5 is a majority element because 5 > 9/2 is true.
# Example 2:
#
# Input: nums = [10,100,101,101], target = 101
# Output: false
# Explanation:
# The value 101 appears 2 times and the length of the array is 4.
# Thus, 101 is not a majority element because 2 > 4/2 is false.

import collections


class Solution:
    # O(n) Spcae and O(n) Time
    def isMajorityElement(self, nums, target):
        dict = collections.Counter(nums)
        if len(nums) == 1:
            return nums[0] == target

        k = nums[len(nums) // 2]
        if dict[k] > len(nums) // 2:
            return True

        return False

    # O(1) Space and O(n) Time

    def isMajorityElement2(self, nums, target):

        leftIdx = self.search(nums, target, True)
        rightIdx = self.search(nums, target, False)
        if not leftIdx and not rightIdx:
            return False
        if rightIdx - leftIdx + 1 > len(nums) / 2:
            return True
        return False

    def search(self, nums, target, isLeft):
        left = 0
        right = len(nums) - 1

        if isLeft:
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    if mid != 0:
                        if nums[mid - 1] != target:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return None
        else:
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    if mid != len(nums) - 1:
                        if nums[mid + 1] != target:
                            return mid
                        else:
                            left = mid + 1
                    else:
                        return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return None
