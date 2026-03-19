class Solution:
    def prevSmaller(self, arr):
        stack = []
        result = []
        
        for num in arr:
            # Remove elements >= current number
            while stack and stack[-1] >= num:
                stack.pop()
            
            # If stack empty, no smaller element
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            # Push current element
            stack.append(num)
        
        return result
