class Solution:
    def permute(self,nums: list[int]) -> list[list[int]]:
        res = []

        def helper(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num not in path:
                    path.append(num)      # choose
                    helper(path)          # explore
                    path.pop()            # unchoose (backtrack)

        helper([])
        
        return res
