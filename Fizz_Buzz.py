# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for
# the multiples of five output “Buzz”. For numbers which are multiples of both three
# and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        res = []
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        for i in range(1, n + 1):
            curr = []

            for key in fizz_buzz_dict.keys():
                if i % key == 0:
                    curr.append(fizz_buzz_dict[key])
            if not curr:
                curr.append(str(i))
            res.append("".join(curr))

        return res