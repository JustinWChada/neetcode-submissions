import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s_clean = re.sub(r'[^a-zA-Z]', '', s)

        n = len(s)
        j = n-1
        i = 0

        while i < n:
            if not s[i].isalnum():
                i +=1
                continue
            
            if not s[j].isalnum():
                j -=1
                continue

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
