class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)

        for i in range(n):
            lb = 0
            ub = len(matrix[i]) - 1

            if matrix[i][ub] < target:
                continue
            else:
                while lb <= ub:
                    mid = lb + ((ub-lb) // 2)

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        lb = mid + 1
                    elif matrix[i][mid] > target:
                        ub = mid -1
        
        return False
