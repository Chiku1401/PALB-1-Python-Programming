"""
Balancing consonants and vowels ratio.
"""

# Q14: Balanced consonants and vowels ratio
class Solution:
    def countBalanced(self, arr):
        def score(s):
            v = set('aeiou')
            sc = 0
            for ch in s:
                if ch in v:
                    sc += 1
                else:
                    sc -= 1
            return sc
        
        prefix = 0
        res = 0
        
        freq = {0: 1}
        
        for s in arr:
            prefix += score(s)
            
            if prefix in freq:
                res += freq[prefix]
            
            freq[prefix] = freq.get(prefix, 0) + 1
        
        return res