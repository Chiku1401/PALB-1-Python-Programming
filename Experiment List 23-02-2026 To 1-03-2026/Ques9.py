#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

class Solution:
    def isSubset(self, a, b):
        freq = {}

        # Count elements of a
        for num in a:
            freq[num] = freq.get(num, 0) + 1

        # Check elements of b
        for num in b:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1

        return True
