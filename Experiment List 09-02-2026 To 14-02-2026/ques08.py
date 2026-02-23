'''You are given an m x n integer matrix matrix with the following two properties: 
•	Each row is sorted in non-decreasing order. 
•	The first integer of each row is greater than the last integer of the previous row. 
Given an integer target, return true if target is in matrix or false otherwise. You must write a solution in O(log(m * n)) time complexity
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid // n][mid % n]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
