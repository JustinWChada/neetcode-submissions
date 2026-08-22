class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        
        nums_set_len = len(nums_set)
        nums_len = len(nums)

        if nums_set_len == nums_len:
            return False
        
        return True