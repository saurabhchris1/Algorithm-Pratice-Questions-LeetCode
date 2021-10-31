# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
#
# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
#
# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


class Solution:
    def isRobotBounded(self, instructions):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        idx = 0
        x = y = 0

        for i in instructions:

            if i == 'L':
                idx = (idx + 3) % 4
            elif i == 'R':
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        return (x == 0 and y == 0) or idx != 0