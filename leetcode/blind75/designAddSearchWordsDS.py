# Problem: https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Time complexity: O(n^2)
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

    def lookup(self, word: str) -> any:
        if len(word) == 0:
            return self

        nextCh: str = word[0]

        if nextCh == ".":
            for k, v in self.children.items():
                result: TrieNode = self.children[k].lookup(word[1:])
                if result is not None and result.isTerminal: return result

        if nextCh not in self.children:
            return None

        return self.children[nextCh].lookup(word[1:])



class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.insert(word)
    
    def search(self, word: str) -> bool:
        result: Optional[TrieNode] = self.root.lookup(word)
        return result is not None and result.isTerminal


def main():
    wordDict: WordDictionary = WordDictionary()

    wordDict.addWord("bad")
    wordDict.addWord("dad")
    wordDict.addWord("mad")
    print(wordDict.search("pad")) # False
    print(wordDict.search("bad")) # True
    print(wordDict.search(".ad")) # True
    print(wordDict.search("b..")) # True

    print("------------------------------------------------------")

    wordDict = WordDictionary()
    wordDict.addWord("at")
    wordDict.addWord("and")
    wordDict.addWord("an")
    wordDict.addWord("add")
    print(wordDict.search("a")) # False
    print(wordDict.search(".at")) # False
    wordDict.addWord("bat")
    print(wordDict.search(".at")) # True
    print(wordDict.search("an.")) # True
    print(wordDict.search("a.d.")) # False
    print(wordDict.search("b.")) # False
    print(wordDict.search("a.d")) # True
    print(wordDict.search(".")) # False


if __name__ == '__main__':
    main()
