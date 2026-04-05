"""
Previous Smaller Element
"""

class Solution:
    def prevSmaller(self, arr):
        stack = []
        result = []
        
        for num in arr:
            # Pop elements that are greater than or equal to the current number
            while stack and stack[-1] >= num:
                stack.pop()
                
            # If the stack becomes empty, there's no smaller element to the left
            if not stack:
                result.append(-1)
            else:
                # The top of the stack is the nearest smaller element
                result.append(stack[-1])
                
            # Push the current number onto the stack for the next iterations
            stack.append(num)
            
        return result
