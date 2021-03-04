# Given an unsorted array of integers nums, return the length
# of the longest consecutive elements sequence.
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        longest = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                currentNum = num
                current = 1

                while currentNum + 1 in numSet:
                    currentNum += 1
                    current += 1

                longest = max(longest, current)

        return max(longest, current)

    def longestConsecutive1(self, nums):
        if not nums:
            return 0
        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:

                if nums[i] == nums[i - 1] + 1:
                    current += 1
                else:
                    longest = max(current, longest)
                    current = 1

        return max(longest, current)
