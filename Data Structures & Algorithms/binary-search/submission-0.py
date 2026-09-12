class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1

        while lb <= ub:
            mid = lb + ((ub - lb) // 2)

            if nums[mid] > target:
                ub = mid - 1
            elif nums[mid] < target:
                lb = mid + 1
            else:
                return mid
        
        return -1
            