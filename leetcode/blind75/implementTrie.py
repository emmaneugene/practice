# Problem: https://leetcode.com/problems/implement-trie-prefix-tree/

# Time complexity: O(n) lookup, insert
# Space complexity: O(n)

from typing import Optional


class TrieNode:
    def __init__(self) -> None:
        self.isTerminal: bool = False
        self.children: dict[str, any] = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.isTerminal = True

        if len(word) > 0:
            if word[0] not in self.children:
                self.children[word[0]] = TrieNode()

            self.children[word[0]].insert(word[1:])

    def lookup(self, word: str):
        if len(word) == 0:
            return self

        if word[0] not in self.children:
            return None

        return self.children[word[0]].lookup(word[1:])


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        node: Optional[TrieNode] = self.root.lookup(word)

        return node is not None and node.isTerminal

    def startsWith(self, prefix: str) -> bool:
        node: Optional[TrieNode] = self.root.lookup(prefix)

        return node is not None


def main():
    t: Trie = Trie()

    t.insert("apple")
    print(t.search("apple"))  # true
    print(t.search("app"))  # false
    t.insert("app")
    print(t.search("app"))  # true


if __name__ == "__main__":
    main()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
