class PrefixTree:

    def __init__(self):
        self.root = {}
        self.end = "*"

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr[self.end] = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr:
                return False
            curr = curr[char]

        return self.end in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]

        return True