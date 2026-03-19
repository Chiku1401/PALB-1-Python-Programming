# Count Unique Vowel Strings

class Solution:
    def vowelCount(self, s):
        from collections import Counter
        from math import factorial
        
        vowels = 'aeiou'
        freq = Counter(s)
        
        counts = []
        for v in vowels:
            if freq[v] > 0:
                counts.append(freq[v])
        
        if not counts:
            return 0
        
        total = 1
        for c in counts:
            total *= c
        
        return total * factorial(len(counts))