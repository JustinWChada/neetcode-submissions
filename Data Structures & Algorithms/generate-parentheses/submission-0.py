class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def helper(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                helper(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(')')
                helper(openN, closedN + 1)
                stack.pop()
        
        helper(0,0)
        return res
