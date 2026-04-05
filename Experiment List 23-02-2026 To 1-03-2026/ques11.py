"""
Count unique vowel strings.
"""

# Q11: Count unique vowel strings
class Solution:
    def vowelCount(self, s):
        from math import factorial
        
        vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}
        
        for ch in s:
            if ch in vowels:
                vowels[ch] += 1
        
        count = 1
        distinct = 0
        
        for v in vowels.values():
            if v > 0:
                count *= v
                distinct += 1
        
        if distinct == 0:
            return 0
        
        return count * factorial(distinct)
