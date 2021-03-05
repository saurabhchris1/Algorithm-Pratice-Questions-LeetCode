# Given an array of characters, compress it in-place.
#
# The length after compression must always be smaller than or equal to the original array.
#
# Every element of the array should be a character (not int) of length 1.
#
# After you are done modifying the input array in-place, return the new length of the array.
#
# Follow up:
# Could you solve it using only O(1) extra space?
#
# Input:
# ["a","a","b","b","c","c","c"]
#
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
#
#
# Input:
# ["a"]
#
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
#
# Explanation:
# Nothing is replaced.
#
#
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
#
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array


class Solution:
    def compress(self, chars):
        write, anchor = 0, 0

        for i, char in enumerate(chars):

            if i + 1 == len(chars) or chars[i] != chars[i + 1]:
                chars[write] = chars[anchor]
                write += 1

                if i > anchor:

                    for digit in str(i - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = i + 1

        return write
