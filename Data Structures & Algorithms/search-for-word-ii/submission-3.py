class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word

        ROWS = len(board)
        COLS = len(board[0])

        res = []

        def dfs(r, c, node):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or board[r][c] not in node.children
            ):
                return

            ch = board[r][c]
            node = node.children[ch]

            if node.word:
                res.append(node.word)
                node.word = None

            board[r][c] = "#"

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = ch

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res