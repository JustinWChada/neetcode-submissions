import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        if not tokens: return 0

        stk = []

        op_str= "+-*/"

        for i, item in enumerate(tokens):

            if item in "+-*/":
                b = stk.pop()
                a = stk.pop()
                res = 0

                if item == "+":
                    res = a + b
                elif item == "-":
                    res = a - b
                elif item == "*":
                    res = a * b
                elif item == "/":
                    res = a / b

                    if res < 0:
                        res = math.ceil(res)
                    elif res > 0:
                        res = math.floor(res)

                stk.append(res)

            else: 
                stk.append(int(item))

        return int(stk[0])