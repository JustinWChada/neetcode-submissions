class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(start):
            if start == len(s):
                res.append(subset.copy())
                return

            for end in range(start, len(s)):
                curr = s[start:end + 1]

                if curr == curr[::-1]:
                    subset.append(curr)

                    dfs(end + 1)

                    subset.pop()

        dfs(0)
        return res