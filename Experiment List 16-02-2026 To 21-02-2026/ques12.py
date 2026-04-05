"""
Maximize Minimum Difference
"""

class Solution:
    def maxMinDiff(self, a, k):
        # 1. Sort the array so we can greedily pick elements sequentially
        a.sort()
        n = len(a)
        
        # 2. Helper function to check if a specific 'target_diff' is achievable
        def can_place(target_diff):
            count = 1
            last_placed = a[0]
            
            for i in range(1, n):
                if a[i] - last_placed >= target_diff:
                    count += 1
                    last_placed = a[i]
                    # Early exit if we've successfully placed 'k' elements
                    if count == k:
                        return True
                        
            return count >= k

        # 3. Binary search boundaries for the minimum difference
        low = 0  
        high = a[-1] - a[0]  
        ans = 0
        
        # 4. Binary search over the answer space
        while low <= high:
            mid = low + (high - low) // 2
            
            if can_place(mid):
                ans = mid
                low = mid + 1  # Try to find a larger valid difference
            else:
                high = mid - 1 # Difference is too large, reduce it
                
        return ans