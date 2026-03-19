class Solution:
    def winner(self, arr):
        from collections import Counter
        
        freq = Counter(arr)
        max_votes = max(freq.values())
        
        candidates = [name for name in freq if freq[name] == max_votes]
        winner_name = min(candidates)
        
        return [winner_name, str(max_votes)]