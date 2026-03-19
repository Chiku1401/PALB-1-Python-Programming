class Solution:
    def combinationSum(self, n, k):
        result = []
        
        def backtrack(start, k, target, path):
            # If combination size is k and sum becomes 0
            if k == 0 and target == 0:
                result.append(path[:])
                return
            
            # Stop if invalid
            if k < 0 or target < 0:
                return
            
            # Try numbers from start to 9
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, k - 1, target - num, path)
                path.pop()  # backtrack
        
        backtrack(1, k, n, [])
        return result
