from collections import Counter

class Solution:
    def frequencySort(self, s):
        freq = Counter(s)
        
        # sort by frequency ascending, then lexicographically
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        result = ''.join(char * count for char, count in sorted_chars)
        return result