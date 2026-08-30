class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n-1

        ml = height[0]
        mr = height[r]

        res = 0

        while l < r:
            if ml < mr:
                l += 1
                ml = max(ml, height[l])
                res += ml - height[l]
            else:
                r -= 1
                mr = max(mr, height[r])
                res += mr - height[r]
        
        return res
