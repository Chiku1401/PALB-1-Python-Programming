class Solution:
    def preGreaterEle(self, arr):
        stack = []
        result = []
        
        for num in arr:
            # Remove elements <= current number
            while stack and stack[-1] <= num:
                stack.pop()
            
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            stack.append(num)
        
        return result
