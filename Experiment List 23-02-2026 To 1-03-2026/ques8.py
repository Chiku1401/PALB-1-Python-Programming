"""
Winner of an election.
"""

# Q8: Winner of election
class Solution:
    def winner(self, arr):
        from collections import Counter
        freq = Counter(arr)
        max_votes = max(freq.values())
        candidates = [k for k, v in freq.items() if v == max_votes]
        candidates.sort()
        return [candidates[0], str(max_votes)]
