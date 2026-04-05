"""
132 Pattern
"""

class Solution:
    def has132Pattern(self, arr):
        n = len(arr)
        if n < 3:
            return False
            
        stack = []
        third = float('-inf')  # This represents arr[k] (the "2" in 132)
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            
            # If we find a "1" that is smaller than our established "2", we're done!
            if arr[i] < third:
                return True
                
            # If the current element is greater than the stack's top, 
            # it acts as a "3" and the stack's top acts as a "2".
            # We pop to update our "2" to the largest valid value possible.
            while stack and arr[i] > stack[-1]:
                third = stack.pop()
                
            # Push the current element onto the stack as a potential "3" or "2" for later
            stack.append(arr[i])
            
        return False