# Shortest substring containing all vowels from s1 in s2

class Solution:
    def substrWithVowels(self, s1, s2):
        required = set(s1)
        n = len(s2)
        
        left = 0
        min_len = float('inf')
        freq = {}
        formed = 0
        
        for right in range(n):
            ch = s2[right]
            
            if ch in required:
                freq[ch] = freq.get(ch, 0) + 1
                if freq[ch] == 1:
                    formed += 1
            
            while formed == len(required):
                min_len = min(min_len, right - left + 1)
                
                if s2[left] in required:
                    freq[s2[left]] -= 1
                    if freq[s2[left]] == 0:
                        formed -= 1
                left += 1
        
        return min_len if min_len != float('inf') else -1