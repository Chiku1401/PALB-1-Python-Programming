#Given an array arr[]. Your task is to find the minimum and maximum elementsin the array.

class Solution:
    def getMinMax(self, arr):
        min=arr[0]
        max=arr[0]
        
        for i in range(1,len(arr)):
            if arr[i]<min:
                min=arr[i]
            if arr[i]>max:
                max=arr[i]
        return [min,max]
