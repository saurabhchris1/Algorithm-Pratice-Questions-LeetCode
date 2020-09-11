# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
#
# Example 1:
# Input: nums = [4, 2, 3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
#
# Example 2:
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.

class Solution:
    def checkPossibility(self, nums):

        idx = None

        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:

                if idx is not None:
                    return False

                idx = i

        if idx == None:
            return True

        if idx == 0:
            return True
        if idx == len(nums) - 2:
            return True

        if nums[idx] <= nums[idx + 2]:
            return True

        if nums[idx - 1] <= nums[idx + 1]:
            return True

        return False
