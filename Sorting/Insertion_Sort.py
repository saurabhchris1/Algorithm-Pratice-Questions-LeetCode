class Soltuion:
    def insertion_sort(self, nums):

        for i in range(1, len(nums)):

            j = i
            while j > 0 and nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1

        return nums


if __name__ == "__main__":
    arr = [2, 6, 4, 5, 1, 0, 35]
    print (Soltuion().insertion_sort(arr))
