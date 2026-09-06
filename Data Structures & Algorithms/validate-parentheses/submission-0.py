class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{',

        }

        stk = []

        for c in s:
            if c not in hashMap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()

                    if popped != hashMap[c]:
                        return False
            
        return not stk
