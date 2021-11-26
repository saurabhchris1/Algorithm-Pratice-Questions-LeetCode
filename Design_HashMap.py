# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
#
#
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
#
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):

        for kv in self.bucket:
            if key == kv[0]:
                return kv[1]
        else:
            return -1

    def delete(self, key):

        for idx, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[idx]
                break

    def update(self, key, value):
        found = False

        for idx, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[idx] = (key, value)
                found = True

        if not found:
            self.bucket.append((key, value))


class MyHashMap:

    def __init__(self):
        self.keyspace = 2096
        self.hashtable = [Bucket() for _ in range(self.keyspace)]

    def put(self, key: int, value: int) -> None:
        hashedKey = key % self.keyspace
        self.hashtable[hashedKey].update(key, value)

    def get(self, key: int) -> int:
        hashedKey = key % self.keyspace
        return self.hashtable[hashedKey].get(key)

    def remove(self, key: int) -> None:
        hashedKey = key % self.keyspace
        self.hashtable[hashedKey].delete(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)