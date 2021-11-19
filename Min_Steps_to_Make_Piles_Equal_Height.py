# Alexa is given n piles of equal or unequal heights. In one step, Alexa can remove any number
# of boxes from the pile which has the maximum height and try to make it equal to the one which
# is just lower than the maximum height of the stack. Determine the minimum number of steps
# required to make all of the piles equal in height.
#
# Example 1:
#
# Input: piles = [5, 2, 1]
# Output: 3
# Explanation:
# Step 1: reducing 5 -> 2 [2, 2, 1]
# Step 2: reducing 2 -> 1 [2, 1, 1]
# Step 3: reducing 2 -> 1 [1, 1, 1]
# So final number of steps required is 3.
#
# Let's take an example.
# Input  : [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
# Output : 15
# After sorting in reverse, we have...
# [4, 4, 3, 3, 3, 2, 2, 2, 1] --> (2 steps to transform the 4's) --> The 3's must wait for 2 numbers
# before it to finish their reduction
# [3, 3, 3, 3, 3, 2, 2, 2, 1] --> (5 steps to transform the 3's) --> The 2's must wait for 5 numbers
# before it to finish their reduction
# [2, 2, 2, 2, 2, 2, 2, 2, 1] --> (8 steps to transform the 2's) --> The 1's must wait for 8 numbers
# before it to finish their reduction
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
# Why did we sort in reverse? Because we want to process the maximum / largest number(s) first, which
# is what the question wants. At each step, we can only reduce the largest number(s) to the value of
# the 2nd-largest number(s)
#
# The main idea throughout the algorithm is that - Every time I meet a different number in the
# reverse-sorted array, I have to count how many numbers came before it. This represents the number
# of steps that was taken to reduce these numbers to the current number

# Reference https://leetcode.com/discuss/interview-question/364618/ by Wei_lun

def min_steps_balance(piles):
    """
    Time  : O(N log N)
    Space : O(1), where N = len(s)
    """

    # EDGE CASE
    if len(piles) < 2:
        return 0

    # SORT THE BLOCKS
    piles = sorted(piles, reverse=True)

    # COUNT THE STEPS WE NEED
    steps = 0

    # EACH TIME WE SEE A DIFFERENT ELEMENT, WE NEED TO SEE HOW MANY ELEMENTS ARE BEFORE IT
    for i in range(1, len(piles)):
        steps += i if piles[i - 1] != piles[i] else 0

    return steps


if __name__ == "__main__":
    print(min_steps_balance([50]) == 0)
    print(min_steps_balance([10, 10]) == 0)
    print(min_steps_balance([5, 2, 1]) == 3)
    print(min_steps_balance([4, 2, 1]) == 3)
    print(min_steps_balance([4, 5, 5, 4, 2]) == 6)
    print(min_steps_balance([4, 8, 16, 32]) == 6)
    print(min_steps_balance([4, 8, 8]) == 2)
    print(min_steps_balance([4, 4, 8, 8]) == 2)
    print(min_steps_balance([1, 2, 2, 3, 3, 4]) == 9)
    print(min_steps_balance([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)