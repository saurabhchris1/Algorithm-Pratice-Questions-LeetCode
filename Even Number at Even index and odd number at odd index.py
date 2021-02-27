# Given an array of size n containing equal number of
# odd and even numbers. The problem is to arrange the
# numbers in such a way that all the even numbers get
# the even index and odd numbers get the odd index.
# Required auxiliary space is O(1).
#
# Examples :
#
# Input : arr[] = {3, 6, 12, 1, 5, 8}
# Output : 6 3 12 1 8 5
#
# Input : arr[] = {10, 9, 7, 18, 13, 19, 4, 20, 21, 14}
# Output : 10 9 18 7 20 19 4 13 14 21


def oddEven(nums):
    even = 0
    odd = 1

    while True:

        while even < len(nums) and nums[even] % 2 == 0:
            even += 2
        while odd < len(nums) and nums[odd] % 2 == 1:
            odd += 2

        if even < len(nums) and odd < len(nums):
            nums[odd], nums[even] = nums[even], nums[odd]

        else:
            break