class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        currLvl = self.root
        for char in word:
            if char not in currLvl:
                currLvl[char] = []
            currLvl = currLvl[char]
        currLvl["*"] = None

    def search(self, word: str) -> bool:
        currLvl = self.root
        for char in word:
            if char not in currLvl:
                return False
            currLvl = currLvl[char]
        if "*" not in currLvl:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        currLvl = self.root
        for char in word:
            if char not in currLvl:
                return False
            currLvl = currLvl[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)