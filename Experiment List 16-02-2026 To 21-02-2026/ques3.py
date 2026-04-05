"""
Minimum operations to halve sum
"""

import heapq

class Solution:
    def minOperations(self, arr):
        total_sum = sum(arr)
        target = total_sum / 2
        
        heap = [-x for x in arr]
        heapq.heapify(heap)
        
        steps = 0
        
        while total_sum > target:
            largest = -heapq.heappop(heap)
            half = largest / 2
            
            total_sum -= half
            heapq.heappush(heap, -half)
            
            steps += 1
        
        return steps