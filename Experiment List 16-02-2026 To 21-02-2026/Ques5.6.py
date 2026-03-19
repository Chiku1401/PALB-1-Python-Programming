class Solution:
    def has132Pattern(self, arr):
        stack = []
        third = float('-inf')

        # Traverse from right to left
        for i in range(len(arr) - 1, -1, -1):
            
            if arr[i] < third:
                return True
            
            while stack and arr[i] > stack[-1]:
                third = stack.pop()
            
            stack.append(arr[i])

        return False
