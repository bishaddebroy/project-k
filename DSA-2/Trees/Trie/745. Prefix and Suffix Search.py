class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, w, i):
        curr = self.root
        for ch in w:
            c = ord(ch) - ord('a')
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.index = i

    def search(self, w):
        curr = self.root
        for ch in w:
            c = ord(ch) - ord('a')
            if not curr.children[c]:
                return -1
            curr = curr.children[c]
        return curr.index

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.char = '{'
        for i, w in enumerate(words):
            wLen = len(w)
            for j in range(wLen):
                suff = w[j:]
                for k in range(wLen + 1):
                    pref = w[:k]
                    self.trie.addWord(pref + self.char + suff, i)


    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(pref + self.char + suff)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)