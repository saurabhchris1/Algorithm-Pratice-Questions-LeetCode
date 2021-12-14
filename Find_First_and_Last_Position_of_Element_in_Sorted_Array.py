# Given an array of integers nums sorted in non-decreasing order, find the starting and
# ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Example
# 2:
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
# Example
# 3:
#
# Input: nums = [], target = 0
# Output: [-1, -1]

class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]
        res[0] = self.find(nums, target, True)
        res[1] = self.find(nums, target, False)

        return res

    def find(self, nums, target, first):

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                if first:
                    if mid > 0 and nums[mid] == nums[mid - 1]:
                        end = mid - 1
                    else:
                        return mid
                else:
                    if mid < end and nums[mid] == nums[mid + 1]:
                        start = mid + 1
                    else:
                        return mid
        return -1