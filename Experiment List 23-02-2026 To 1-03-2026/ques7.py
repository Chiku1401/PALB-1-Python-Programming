"""
Count pairs of strings with exactly one mismatch.
"""

# Q7: Count pairs with one mismatch
class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        
        freq = defaultdict(int)
        res = 0
        
        for s in arr:
            seen = set()
            for i in range(len(s)):
                pattern = s[:i] + '*' + s[i+1:]
                
                if pattern not in seen:
                    res += freq[pattern]
                    freq[pattern] += 1
                    seen.add(pattern)
        
        return res
