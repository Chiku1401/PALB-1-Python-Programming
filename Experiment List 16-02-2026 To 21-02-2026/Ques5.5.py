class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        total = 0
        
        for i in range(n - 1, -1, -1):
            # Remove elements >= current
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if not stack:
                next_smaller = n
            else:
                next_smaller = stack[-1]
            
            total += next_smaller - i
            
            stack.append(i)
        
        return total
