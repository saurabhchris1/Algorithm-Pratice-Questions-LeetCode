# Design a time-based key-value data structure that can store multiple values for the same key at
# different time stamps and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with
# timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the
# largest timestamp_prev. If there are no values, it returns "".
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and
# timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        timeValues = self.store[key]

        if not timeValues:
            return ""
        left = timeValues[0]
        right = timeValues[-1]

        if timestamp > right[0]:
            return right[1]

        if timestamp < left[0]:
            return ""

        left = 0
        right = len(timeValues) - 1

        while left <= right:

            mid = left + (right - left) // 2
            currTime = timeValues[mid][0]

            if currTime == timestamp:
                return timeValues[mid][1]
            elif currTime > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return timeValues[right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)