# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]


if __name__ == "__main__":
    example1 = ["aa", "a"]
    example2 = ["aa", ""]
    example3 = ["flower", "flow", "flight"]
    example4 = ["dog", "racecar", "car"]
    example5 = []

    print("longest common prefix  for " + str(example1) + " is : " + longestCommonPrefix(example1))
    print("longest common prefix  for " + str(example2) + " is : " + longestCommonPrefix(example2))
    print("longest common prefix  for " + str(example3) + " is : " + longestCommonPrefix(example3))
    print("longest common prefix  for " + str(example4) + " is : " + longestCommonPrefix(example4))
    print("longest common prefix  for " + str(example5) + " is : " + longestCommonPrefix(example5))
