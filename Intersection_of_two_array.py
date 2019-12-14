import collections


class Solution:
    def intersection(self, nums1, nums2):
        nums_dict_1 = collections.Counter(nums1)
        nums_dict_2 = collections.Counter(nums2)

        arr = []

        for num in nums_dict_1.keys():
            if num in nums_dict_2:
                arr.append(num)

        return arr
