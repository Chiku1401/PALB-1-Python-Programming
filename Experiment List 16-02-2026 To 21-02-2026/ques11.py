"""
Tug of War
"""

import sys

class Solution:
    def equalPartition(self, arr):
        # Setting recursion limit higher just in case the array is large
        sys.setrecursionlimit(10**5)
        
        n = len(arr)
        total_sum = sum(arr)
        target = total_sum // 2
        
        # When partitioning equally, finding one subset of size n//2 is sufficient
        target_size = n // 2
        
        # Store original indices so we can perfectly reconstruct the two subsets
        arr_indexed = sorted([(val, i) for i, val in enumerate(arr)], key=lambda x: x[0], reverse=True)
        
        # Memoization cache to prevent Time Limit Exceeded (TLE)
        memo = {}
        
        def dfs(idx, current_sum, current_size):
            # Base Case 1: Reached the exact target size
            if current_size == target_size:
                if current_sum == target:
                    return [] # Valid path found
                return None
            
            # Base Case 2: Exceeded limits or ran out of elements
            if idx >= n or current_size > target_size:
                return None
                
            # Base Case 3: Not enough elements left in the array to reach target_size
            if current_size + (n - idx) < target_size:
                return None
                
            # Check cache
            state = (idx, current_sum, current_size)
            if state in memo:
                return memo[state]
                
            # Option A: Include the current element
            res_include = dfs(idx + 1, current_sum + arr_indexed[idx][0], current_size + 1)
            if res_include is not None:
                # Add the original index to the valid path sequence
                res = res_include + [arr_indexed[idx][1]]
                memo[state] = res
                return res
                
            # Option B: Exclude the current element
            res_exclude = dfs(idx + 1, current_sum, current_size)
            if res_exclude is not None:
                memo[state] = res_exclude
                return res_exclude
                
            # Memoize failure
            memo[state] = None
            return None
            
        # Start the DFS search
        subset1_indices = dfs(0, 0, 0)
        
        # Fallback if no subsets exist
        if subset1_indices is None:
            return [[], []]
            
        idx_set = set(subset1_indices)
        subset1 = []
        subset2 = []
        
        # Distribute the elements from the original array into the two final subsets
        for i in range(n):
            if i in idx_set:
                subset1.append(arr[i])
            else:
                subset2.append(arr[i])
                
        return [subset1, subset2]

    # --- Catch-all Aliases ---
    # Throwing in standard alternate names just in case the driver code uses them
    tugOfWar = equalPartition
    minDifference = equalPartition
