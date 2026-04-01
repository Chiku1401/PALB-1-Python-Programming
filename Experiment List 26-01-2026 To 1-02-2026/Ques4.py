#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n]
#inclusive.
#There is only one repeated number in nums, return this repeated number.
#You must solve the problem without modifying the array nums and using only constant extra space.

class Solution:
    def minDifference(self, arr):
        # Convert time to seconds
        times = []
        for t in arr:
            h, m, s = map(int, t.split(":"))
            total = h * 3600 + m * 60 + s
            times.append(total)
        
        # Sort times
        times.sort()
        
        # Find minimum difference
        ans = float('inf')
        
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i-1])
        
        # Circular difference (last to first)
        day = 24 * 3600
        ans = min(ans, day - times[-1] + times[0])
        
        return ans