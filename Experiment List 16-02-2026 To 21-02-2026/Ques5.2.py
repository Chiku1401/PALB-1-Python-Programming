class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        # Create intervals
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))
        
        # Sort by start
        intervals.sort()
        
        count = 0
        i = 0
        curr_end = 0
        
        # Greedy covering
        while curr_end < n:
            farthest = curr_end
            
            while i < len(intervals) and intervals[i][0] <= curr_end:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1
            
            if farthest == curr_end:
                return -1
            
            count += 1
            curr_end = farthest
        
        return count
