# Serialization is the process of converting a data structure or object into a sequence of bits so that
# it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed
# later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node
# has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]


# Definition for a Node.

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque

class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ""

        res = []
        queue = deque([root])
        print(root.val)
        while queue:
            level = len(queue)
            for i in range(level):

                node = queue.popleft()
                if node == "$":
                    res.append("$")
                    continue
                res.append(str(node.val))

                for child in node.children:
                    queue.append(child)

                if i != level - 1:
                    queue.append("$")
            res.append("#")

        return " ".join(res)

    def _deserializeHelper(self, data, rootNode):

        prevLevel, currentLevel = deque(), deque()
        currentLevel.append(rootNode);
        parentNode = rootNode;

        for i in range(1, len(data)):
            if data[i] == '#':

                prevLevel = currentLevel;
                currentLevel = deque()
                parentNode = prevLevel.popleft() if prevLevel else None;

            else:
                if data[i] == '$':
                    parentNode = prevLevel.popleft() if prevLevel else None;
                else:
                    childNode = Node(data[i], []);
                    currentLevel.append(childNode);
                    parentNode.children.append(childNode);

    def deserialize(self, data: str) -> 'Node':

        if not data:
            return None
        data = data.split(" ")
        rootNode = Node(data[0], [])
        self._deserializeHelper(data, rootNode)
        return rootNode

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))