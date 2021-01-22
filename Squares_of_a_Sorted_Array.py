# Given an array of integers A sorted in non-decreasing order, return an
# array of the squares of each number, also in sorted non-decreasing order.
#
# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


class Solution:
    def sortedSquares(self, nums):
        N = len(nums)
        j = 0
        while j < N and nums[j] < 0:
            j += 1

        i = j - 1
        ans = []

        while i >= 0 and j < N:
            if nums[i] ** 2 < nums[j] ** 2:
                ans.append(nums[i] ** 2)
                i -= 1
            else:
                ans.append(nums[j] ** 2)
                j += 1

        while i >= 0:
            ans.append(nums[i] ** 2)
            i -= 1

        while j < N:
            ans.append(nums[j] ** 2)
            j += 1

        return ans
