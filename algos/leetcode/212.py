# Problem: https://leetcode.com/problems/word-search-ii
# tags: blind75, hard

# Time complexity:
# Space complexity:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        """
        Using Trie + DFS for multiple word search
        Time: O(M*N*4^L + W*L) where W = number of words
        Space: O(W*L) for trie
        """
        if not board or not board[0] or not words:
            return []

        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(row, col, node):
            if node.word:
                result.append(node.word)
                node.word = None  # Avoid duplicates

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            char = board[row][col]
            if char not in node.children:
                return

            board[row][col] = "#"  # Mark visited
            next_node = node.children[char]

            # Search in 4 directions
            dfs(row + 1, col, next_node)
            dfs(row - 1, col, next_node)
            dfs(row, col + 1, next_node)
            dfs(row, col - 1, next_node)

            board[row][col] = char  # Backtrack

        # Start DFS from each cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i, j, root)

        return result


def main():
    s = Solution()

    print(
        s.findWords(
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea,", "eat", "rain"],
        )
    )  # Expected: ["oath", "eat"]

    print(s.findWords([["a", "b"], ["c", "b"]], ["abcb"]))  # Expected: []


if __name__ == "__main__":
    main()
