# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
#
# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number
# of consecutive 1s is 4.
#
# Input: nums = [1,0,1,1,0,1]
# Output: 4
#
# Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all
# numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

class Solution:
    def findMaxConsecutiveOnesBruteForce(self, nums):
        longest = 0

        for i in range(len(nums)):
            numOfZeros = 0
            for j in range(i, len(nums)):

                if numOfZeros == 2:
                    break
                if nums[j] == 0:
                    numOfZeros += 1
                if numOfZeros <= 1:
                    longest = max(longest, j - i + 1)
        return longest

    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        longest = 0
        numOfZeros = 0

        while right < len(nums):

            if nums[right] == 0:
                numOfZeros += 1

            while numOfZeros == 2:

                if nums[left] == 0:
                    numOfZeros -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest