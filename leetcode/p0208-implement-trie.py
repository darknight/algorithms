#!/usr/bin/env python3

class TrieNode:
    def __init__(self, data: str):
        self.data = data
        self.children = [None] * 26
        self.is_ending = False


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str):
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if p.children[idx] is None:
                p.children[idx] = TrieNode(ch)
            p = p.children[idx]
        p.is_ending = True

    def search(self, word: str):
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if p.children[idx] is None:
                return False
            p = p.children[idx]
        return p.is_ending

    def startsWith(self, prefix: str):
        p = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if p.children[idx] is None:
                return False
            p = p.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
if __name__ == '__main__':
    trie = Trie()
    #trie.insert("ab")
    #print(trie.startsWith("a"))
    #print(trie.search("a"))

    trie.insert("abc")
    print(trie.search("abc"))
    print(trie.search("ab"))

    trie.insert("ab")
    print(trie.search("ab"))

    trie.insert("ab")
    print(trie.search("ab"))

