# You should design a data structure that supports adding new words and
# finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) adds word to the data structure, it can be matched later.
# bool search(word) returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
#
# Example:
#
# Input
# ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
# [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
# Output
# [null, null, null, null, false, true, true, true]
#
# Explanation
# WordDictionary
# wordDictionary = new
# WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord
        self.children = children


class WordDictionary:

    def __init__(self):
        self.trie = Node(False, {})

    def addWord(self, word):
        trie = self.trie
        current = trie
        for char in word:
            if not char in current.children:
                current.children[char] = Node(False, {})
            current = current.children[char]
        current.isWord = True

    def search(self, word):
        current = self.trie

        def helper(node, word):
            for idx, char in enumerate(word):

                if not char in node.children:
                    if char == '.':
                        for x in node.children:
                            if helper(node.children[x], word[idx + 1:]):
                                return True

                    return False
                else:
                    node = node.children[char]
            if node.isWord:
                return True
            return False

        return helper(current, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
