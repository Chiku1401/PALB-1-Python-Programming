#You are given an array of integers arr[]. You have to reverse the given array.



class Solution:
    def reverseArray(self, arr):
        # code herep
        n=len(arr)
        for i in range(n//2):
            arr[i] , arr[n-i-1] = arr[n-i-1],arr[i]
