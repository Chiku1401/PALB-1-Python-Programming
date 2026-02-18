#Given an array arr[]. The task is to find the largest element and return it.

class Solution:
    def largest(self, arr):
        # Assume the first element is the largest
        max_val = arr[0]
        
        # Compare with every other element
        for num in arr:
            if num > max_val:
                max_val = num
                
        return max_val
