"""
Sort string by frequency (ascending, lexicographical tie).
"""

# Q5: Sort by frequency
from collections import Counter

class Solution:
    def frequencySort(self, s):
        freq = Counter(s)
        unique_chars = list(freq.keys())
        unique_chars.sort(key=lambda x: (freq[x], x))
        
        res = []
        for char in unique_chars:
            res.append(char * freq[char])
            
        return "".join(res)
