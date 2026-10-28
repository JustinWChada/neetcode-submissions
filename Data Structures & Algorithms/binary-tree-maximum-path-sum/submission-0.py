class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # path using current node as highest point
            self.res = max(
                self.res,
                node.val + left + right
            )

            # value returned to parent
            return node.val + max(left, right)

        dfs(root)
        return self.res
