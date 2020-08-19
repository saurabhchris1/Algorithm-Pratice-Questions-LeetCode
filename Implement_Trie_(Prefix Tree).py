# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true


class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord
        self.children = children


class Trie:

    def __init__(self):
        self.trie = Node(False, {})

    def insert(self, word) -> None:
        trie = self.trie
        current = trie
        for char in word:
            if not char in current.children:
                current.children[char] = Node(False, {})
            current = current.children[char]
        current.isWord = True

    def search(self, word):
        current = self.trie
        for char in word:
            if not char in current.children:
                return False
            current = current.children[char]
        print(self.trie.children)
        if current.isWord:
            return True
        return False

    def dfs(self, node, prefix, words):

        if node.isWord:
            words.append(prefix)
        for char in node.children:
            self.dfs(node.children[char], prefix + char, words)

    def startsWith(self, prefix: str):
        current = self.trie
        for char in prefix:
            if not char in current.children:
                return False
            current = current.children[char]

        words = []
        self.dfs(current, prefix, words)
        if words:
            return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
