class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res = [0] * n

        stk = []
        i = 0

        for i, item in enumerate(temperatures):
            while stk and stk[-1][0] < item:
                stk_t, stk_i = stk.pop()
                res[stk_i] = i -stk_i
            
            stk.append((item, i))
        
        return res
            
