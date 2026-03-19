# 7. Count pairs of strings with exactly one mismatch

class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        
        pattern_count = defaultdict(int)
        total_pairs = 0
        
        for word in arr:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                total_pairs += pattern_count[pattern]
                pattern_count[pattern] += 1
        
        return total_pairs