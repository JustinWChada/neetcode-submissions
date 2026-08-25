class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)#{2, 3, 4, 5, 10, 20}

        res = 0

        for num in numSet:
            prev = num -1
            
            if (prev) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                res = max(length, res)
        
        return res

