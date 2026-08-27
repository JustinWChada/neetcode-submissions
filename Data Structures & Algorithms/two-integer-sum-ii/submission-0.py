class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        i, j= 0, n-1

        while i<n:
            num_i = numbers[i]
            num_j = numbers[j]

            if num_i + num_j == target:
                return [i+1, j+1]
            
            if num_i + num_j > target:
                j -= 1
                continue
            
            if num_i + num_j < target:
                i += 1
                continue
        
        return [0,0]