"""
Check if permutation is substring.
"""

# Q9: Permutation substring
class Solution:
    def search(self, txt, pat):
        n, m = len(txt), len(pat)
        if m > n:
            return False
        
        freq_pat = [0]*26
        freq_txt = [0]*26
        
        for i in range(m):
            freq_pat[ord(pat[i]) - ord('a')] += 1
            freq_txt[ord(txt[i]) - ord('a')] += 1
        
        if freq_pat == freq_txt:
            return True
        
        for i in range(m, n):
            freq_txt[ord(txt[i]) - ord('a')] += 1
            freq_txt[ord(txt[i-m]) - ord('a')] -= 1
            
            if freq_pat == freq_txt:
                return True
        
        return False