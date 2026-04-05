"""
Minimum number of swaps between two binary strings to make them identical.
"""

# Q1: Minimum number of swaps
class Solution:
    def minSwaps(self, s1, s2):
        xy = 0  # s1[i] = 0, s2[i] = 1
        yx = 0  # s1[i] = 1, s2[i] = 0
        
        for i in range(len(s1)):
            if s1[i] == '0' and s2[i] == '1':
                xy += 1
            elif s1[i] == '1' and s2[i] == '0':
                yx += 1
        
        # If total mismatches is odd → impossible
        if (xy + yx) % 2 != 0:
            return -1
        
        # Swaps calculation
        return (xy // 2) + (yx // 2) + 2 * (xy % 2)
