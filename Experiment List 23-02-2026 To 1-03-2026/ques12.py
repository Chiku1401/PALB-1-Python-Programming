"""
Count even letters.
"""

# Q12: Count even letters
class Solution:
    def count(self, s):
        from collections import Counter
        freq = Counter(s)
        return sum(1 for v in freq.values() if v % 2 == 0)
