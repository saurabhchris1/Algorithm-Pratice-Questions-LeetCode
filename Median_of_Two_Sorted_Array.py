# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution:
    def find_median_sorted_arrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.find_median_sorted_arrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)

        start = 0
        end = x

        while start <= end:

            partitionX = (start + end) // 2

            partitionY = ((x + y + 1) // 2) - partitionX

            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float("inf") if partitionX == x else nums1[partitionX]

            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float("inf") if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                end = partitionX - 1
            else:
                start = partitionX + 1


if __name__ == '__main__':
    ex1 = [1, 2]
    ex2 = [3, 4]
    ex3 = [1, 3]
    ex4 = [2]

    print("The median of arrays : " + str(ex1) + " " + str(ex2) + " is : " + str(
        Solution().find_median_sorted_arrays(ex1, ex2)))
    print("The median of arrays : " + str(ex3) + " " + str(ex4) + " is : " + str(
        Solution().find_median_sorted_arrays(ex3, ex4)))
