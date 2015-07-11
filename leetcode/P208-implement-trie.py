class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, char):
        if char in self.children:
            return
        self.children[char] = TrieNode()

    def next(self, char):
        if char in self.children:
            return self.children[char]
        return None

    def is_word_end(self):
        return self.word_end

    def set_word_end(self):
        self.word_end = True

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        root = self.root
        for char in word:
            root.insert(char)
            root = root.next(char)
            assert root
        root.set_word_end()

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        root = self.root
        for char in word:
            root = root.next(char)
            if root is None:
                return False
        if root.is_word_end():
            return True
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        root = self.root
        for char in prefix:
            root = root.next(char)
            if root is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
if __name__ == '__main__':
    trie = Trie()
    #trie.insert("ab")
    #print trie.startsWith("a")
    #print trie.search("a")

    trie.insert("abc")
    print trie.search("abc")
    print trie.search("ab")

    trie.insert("ab")
    print trie.search("ab")

    trie.insert("ab")
    print trie.search("ab")

