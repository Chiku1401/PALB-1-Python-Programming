"""
Max Visible People
"""

class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        # 1. Find the Previous Greater (or Equal) Element for each index
        prev_greater = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                prev_greater[i] = stack[-1]
            stack.append(i)
            
        # 2. Find the Next Greater (or Equal) Element for each index
        next_greater = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(i)
            
        # 3. Calculate the maximum number of visible people
        max_vis = 0
        for i in range(n):
            # The count of people between the left and right boundaries
            vis = next_greater[i] - prev_greater[i] - 1
            if vis > max_vis:
                max_vis = vis
                
        return max_vis
