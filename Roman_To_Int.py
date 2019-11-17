# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II. The number twenty seven is written
# as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However,
# the numeral for four is not IIII. Instead, the number four is written as IV. Because
# the one is before the five we subtract it making four. The same principle applies to
# the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


def roman_to_int(s):
    roman_dict = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}

    num = 0

    if len(s) == 1:
        return roman_dict[s]

    for i in range(len(s)):

        if i != 0:

            if roman_dict[s[i - 1]] < roman_dict[s[i]]:

                num = num + roman_dict[s[i]] - (2 * roman_dict[s[i - 1]])
            else:
                num = num + roman_dict[s[i]]
        else:
            num = num + roman_dict[s[i]]

    return num


if __name__ == '__main__':
    # MMMCMXCIX => 3999
    ex1 = "MMMCMXCIX"
    ex2 = "I"
    ex3 = "IX"
    # "LVIII" => 58
    ex4 = "LVIII"

    print("The roman to int of " + ex1 + " is : " + str(roman_to_int(ex1)))
    print("The roman to int of " + ex2 + " is : " + str(roman_to_int(ex2)))
    print("The roman to int of " + ex3 + " is : " + str(roman_to_int(ex3)))
    print("The roman to int of " + ex4 + " is : " + str(roman_to_int(ex4)))
