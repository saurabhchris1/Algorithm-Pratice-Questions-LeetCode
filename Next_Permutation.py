# Implement next permutation, which rearranges numbers into the lexicographically
# next greater permutation of numbers.
#
# If such an arrangement is not possible, it must rearrange it as the lowest
# possible order (i.e., sorted in ascending order).
#
# The replacement must be in place and use only constant extra memory.
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
#
# Input: nums = [1]
# Output: [1]

class Solution:
    def nextPermutation(self, nums) -> None:

        i = len(nums) - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1)

    def reverse(self, nums, i):
        start = i
        end = len(nums) - 1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1