class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i] #4 = 7-3; 3 = 7-4

            if diff in hashMap: # {} {3: 0}
                return [hashMap[diff], i] # (0,1)
            else:
                hashMap[nums[i]] = i # {3: 0, }
        
        return (0,0)
            