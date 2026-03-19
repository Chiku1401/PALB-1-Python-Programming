
class Solution:
    def search(self, txt, pat):
        n = len(txt)
        k = len(pat)
        
        if k > n:
            return False
        
        # frequency arrays (since lowercase letters only)
        pat_freq = [0] * 26
        win_freq = [0] * 26
        
        for ch in pat:
            pat_freq[ord(ch) - ord('a')] += 1
        
        for i in range(k):
            win_freq[ord(txt[i]) - ord('a')] += 1
        
        if pat_freq == win_freq:
            return True
        
        for i in range(k, n):
            win_freq[ord(txt[i]) - ord('a')] += 1
            win_freq[ord(txt[i-k]) - ord('a')] -= 1
            
            if pat_freq == win_freq:
                return True
        
        return False