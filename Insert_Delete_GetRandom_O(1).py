# Design a data structure that supports all following operations in average O(1) time.
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements
# (it's guaranteed that at least one element exists when this method is called). Each element '
# 'must have the same probability of being returned.
#
# Example:
#
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

import random


class RandomizedSet:

    def __init__(self):
        self.dictVal = {}
        self.listVal = []

    def insert(self, val):

        if val not in self.dictVal:
            self.dictVal[val] = len(self.listVal)
            self.listVal.append(val)
            return True
        return False

    def remove(self, val):

        if val in self.dictVal:
            last_element = self.listVal[-1]
            idx = self.dictVal[val]
            self.listVal[idx] = last_element
            self.dictVal[last_element] = idx
            self.listVal.pop()
            del self.dictVal[val]
            return True
        return False

    def getRandom(self):

        return random.choice(self.listVal)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
