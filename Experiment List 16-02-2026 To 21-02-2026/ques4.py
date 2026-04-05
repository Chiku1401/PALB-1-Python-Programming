"""
Minimum Number of Workers

"""

class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        # Step 1: Convert sprinklers into valid range intervals
        for i in range(n):
            if arr[i] != -1:
                # The sprinkler at 'i' waters from (i - arr[i]) to (i + arr[i])
                start = max(0, i - arr[i])
                end = min(n - 1, i + arr[i])
                intervals.append((start, end))
        
        # Step 2: Sort intervals by start time. 
        # (Sorting by end time descending as a secondary key is a good tie-breaker)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        sprinklers_count = 0
        target = 0
        i = 0
        num_intervals = len(intervals)
        
        # Step 3: Greedily pick the interval that covers the target and extends the furthest
        while target < n:
            max_end = -1
            
            # Find the best sprinkler that starts at or before the 'target'
            while i < num_intervals and intervals[i][0] <= target:
                max_end = max(max_end, intervals[i][1])
                i += 1
            
            # If no sprinkler can cover the current target, it's impossible
            if max_end == -1:
                return -1
            
            # Turn on this sprinkler
            sprinklers_count += 1
            
            # The next point to cover will be just after the furthest reach of the current sprinkler
            target = max_end + 1
            
        return sprinklers_count
