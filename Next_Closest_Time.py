# Given a time represented in the format "HH:MM", form the next closest time by
# reusing the current digits. There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid. For example, "01:34",
# "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Input: time = "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: time = "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller
# than the input time numerically.

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digitSet = set([time[0], time[1], time[3], time[4]])
        time = self.nextTime(time)

        while self.isNotAvailable(time, digitSet):
            time = self.nextTime(time)

        return time

    def nextTime(self, time):
        minutes = int(time[3:])
        hours = int(time[:2])

        minutes += 1

        if minutes >= 60:
            minutes = 0
            hours += 1

        if hours >= 24:
            hours = 0

        return f'{hours:02d}:{minutes:02d}'

    def isNotAvailable(self, time, digits):

        return time[0] not in digits or time[1] not in digits or time[3] not in digits or time[4] not in digits