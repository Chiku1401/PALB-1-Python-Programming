# Count Even Letters

class Solution:
    def count(self, s):
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        even_count = 0
        for value in freq.values():
            if value % 2 == 0:
                even_count += 1
        
        return even_count