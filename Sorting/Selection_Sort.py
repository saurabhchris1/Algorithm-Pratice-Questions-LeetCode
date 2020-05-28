class Solution:

    def Selection_Sort(self, nums):
        current_idx = 0
        while current_idx < len(nums - 1):

            smallest = current_idx

            for i in range(current_idx + 1, len(nums)):

                if nums[i] < nums[smallest]:
                    smallest = i

            nums[i], nums[smallest] = nums[smallest], nums[i]

        return nums
