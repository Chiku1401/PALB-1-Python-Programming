#Given an array arr, rotate the array by one position in clockwise direction.

class Solution:
    def rotate(self, arr):
        if len(arr) == 0:
            return
        
        last = arr.pop()      
        arr.insert(0, last)
