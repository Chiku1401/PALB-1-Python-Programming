"""
Count <= x in rotated array
"""

import bisect

class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        if n == 0:
            return 0
            
        # 1. Find the pivot (the index of the minimum element)
        low, high = 0, n - 1
        while low < high:
            mid = low + (high - low) // 2
            
            if arr[mid] > arr[high]:
                low = mid + 1
            elif arr[mid] < arr[high]:
                high = mid
            else:
                # Safely handle duplicates if they exist in the rotated array
                high -= 1
                
        pivot = low
        
        # 2. Binary search in the two conceptually separated sorted halves
        count = 0
        
        # NOTE: bisect_right returns the *absolute index*. 
        # To get the count of elements, we must subtract the starting boundary.
        
        # Left half (from index 0 up to the pivot)
        if pivot > 0:
            idx_left = bisect.bisect_right(arr, x, 0, pivot)
            count += (idx_left - 0)
            
        # Right half (from the pivot to the end of the array)
        idx_right = bisect.bisect_right(arr, x, pivot, n)
        count += (idx_right - pivot)
        
        return count
