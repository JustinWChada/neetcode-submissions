# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True

        queue = collections.deque()
        queue.append(root)

        low = -1000000000
        max = 1000000000

        def helper(node, low, max):
            if not node: return True
            
            if not (low < node.val and node.val < max):
                return False
            
            return helper(node.left, low, node.val) and helper(node.right, node.val, max)
        
        return helper(root, low, max)

