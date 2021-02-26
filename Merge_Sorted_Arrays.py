# Given two sorted integer arrays nums1 and nums2, merge nums2 into
# nums1 as one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively. You may assume that nums1 has a size equal to m + n
# such that it has enough space to hold additional elements from nums2.
#
# Example 1:
#
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Example 2:
#
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]


class Solution:
    def merge(self, nums1, m, nums2, n):
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        end = len(nums1) - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0 and end >= 0:

            if nums1[p1] >= nums2[p2]:
                nums1[end] = nums1[p1]
                end -= 1
                p1 -= 1
            else:
                nums1[end] = nums2[p2]
                p2 -= 1
                end -= 1
        while p1 >= 0 and end >= 0:
            nums1[end] = nums1[p1]
            p1 -= 1
            end -= 1

        while p2 >= 0 and end >= 0:
            nums1[end] = nums2[p2]
            p2 -= 1
            end -= 1
