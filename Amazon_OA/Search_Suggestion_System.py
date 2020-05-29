# Given an array of strings products and a string searchWord. We want to design a system that suggests at
# most three product names from products after each character of searchWord is typed. Suggested products
# should have common prefix with the searchWord. If there are more than three products with a common prefix
# return the three lexicographically minimums products.
#
# Return list of lists of the suggested products after each character of searchWord is typed.
#
# Example 1:
#
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
# Example 2:
#
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Example 3:
#
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
# Example 4:
#
# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]


class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord
        self.children = children


class Solution:
    def suggestedProducts(self, products, searchWord):

        self.build(products)
        res = []
        prefix_word = ''

        for char in searchWord:
            prefix_word += char
            res.append(sorted(self.autocomplete(prefix_word))[:3])
        return res

    def build(self, words):

        trie = Node(False, {})

        for word in words:

            current = trie
            for char in word:

                if not char in current.children:
                    current.children[char] = Node(False, {})

                current = current.children[char]

            current.isWord = True

        self.trie = trie

    def autocomplete(self, word):

        current = self.trie
        for char in word:

            if not char in current.children:
                return []

            current = current.children[char]

        words = []
        self.dfs(current, word, words)

        return words

    def dfs(self, node, prefix, words):

        if node.isWord:
            words.append(prefix)

        for char in node.children:
            self.dfs(node.children[char], prefix + char, words)

    def dfs_iterative(self, node, prefix, words):
        stack = [(node, prefix)]

        while len(stack):
            (node, prefix) = stack.pop()

            if node.isWord:
                words.append(prefix)

            for char in node.children:
                child = node.children[char]
                stack.append((node.children[char], prefix + char))
