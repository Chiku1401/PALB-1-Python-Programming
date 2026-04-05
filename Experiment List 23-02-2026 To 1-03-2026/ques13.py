"""
Shortest substring containing all vowels.
"""

# Q13: Shortest substring containing all vowels
class Solution:
    def substrWithVowels(self, s1, s2):
        from collections import Counter
        
        need = Counter(s1)
        have = Counter()
        
        required = len(need)
        formed = 0
        
        l = 0
        ans = float('inf')
        
        for r in range(len(s2)):
            ch = s2[r]
            
            if ch in need:
                have[ch] += 1
                if have[ch] == 1:
                    formed += 1
            
            while formed == required:
                ans = min(ans, r - l + 1)
                
                if s2[l] in need:
                    have[s2[l]] -= 1
                    if have[s2[l]] == 0:
                        formed -= 1
                
                l += 1
        
        return ans if ans != float('inf') else -1