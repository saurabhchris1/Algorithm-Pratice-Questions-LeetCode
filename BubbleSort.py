# Bubble Sort


class Solution:

    def bubbleSort(self, nums):

        isSorted = False
        counter = 0

        while not isSorted:
            isSorted = True
            for i in range(len(nums) - 1 - counter):

                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    isSorted = False

        return nums


if __name__ == "__main__":
    arr = [9, 2, 3, 4, 7, 6, 5, 0, 2, 9]
    print (Solution().bubbleSort(arr))
