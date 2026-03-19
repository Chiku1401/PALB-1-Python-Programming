class Solution:
    def minDifference(self, arr):
        def to_seconds(t):
            h, m, s = map(int, t.split(":"))
            return h*3600 + m*60 + s
        
        times = sorted([to_seconds(t) for t in arr])
        min_diff = float('inf')
        
        for i in range(1, len(times)):
            min_diff = min(min_diff, times[i] - times[i-1])
        
        min_diff = min(min_diff, 86400 - times[-1] + times[0])
        
        return min_diff