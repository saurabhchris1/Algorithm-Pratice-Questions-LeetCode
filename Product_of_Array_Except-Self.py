# Given an array nums of n integers where n > 1,  return an array output such that
# output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of
# any prefix or suffix of the array (including the whole array) fits
# in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does
# not count as extra space for the purpose of space complexity analysis.)

class Solution:

    def productExpectSelf(self, nums):

        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1

        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            res[i] *= right

        return res
