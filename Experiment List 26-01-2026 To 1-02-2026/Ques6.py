#Given an array of intervals where intervals[i] = [starti, endi], merge all
#overlapping intervals, and return an array of the non-overlapping intervals that
#cover all the intervals in the input.

class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)
        return arr