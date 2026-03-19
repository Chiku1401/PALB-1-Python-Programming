# Sort an array of strings according to string lengths

class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)