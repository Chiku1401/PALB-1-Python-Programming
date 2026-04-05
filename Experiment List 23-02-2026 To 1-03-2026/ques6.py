"""
Sort array of strings by length (stable).
"""

# Q6: Sort strings by length
class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)
        return arr
