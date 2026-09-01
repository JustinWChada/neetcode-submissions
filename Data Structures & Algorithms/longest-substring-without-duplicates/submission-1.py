class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashMap = set()
        l = 0

        for r in range(len(s)):
            while s[r] in hashMap:
                hashMap.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            res = max(res, w)
            hashMap.add(s[r])
        
        return res
