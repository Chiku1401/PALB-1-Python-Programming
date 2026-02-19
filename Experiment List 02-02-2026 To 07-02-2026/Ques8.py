#You are given an m x n integer matrix matrix with the following two properties: 
#• Each row is sorted in non-decreasing order.
#• The first integer of each row is greater than the last integer of the previous row. Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Map 1D index 'mid' to 2D coordinates [row][col]
            row = mid // n
            col = mid % n
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
