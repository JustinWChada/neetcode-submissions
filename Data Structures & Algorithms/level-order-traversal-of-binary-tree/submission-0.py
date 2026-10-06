# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        queue.append(root)
        res = []
       
        if not root: return []

        while queue:
            n = len(queue)
            level = []

            for i in range(n):
                el = queue.pop(0)
                level.append(el.val)
                queue.append(el.left) if el.left else None
                queue.append(el.right) if el.right else None
            
            res.append(level)
        
        return res
                

                

