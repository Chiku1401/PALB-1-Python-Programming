#Given an array and a range a, b. The task is to partition the array around the range such that the array is divided into three parts.
#1) All elements smaller than a come first.
#2) All elements in range a to b come next.
#3) All elements greater than b appear in the end.
#The individual elements of three sets can appear in any order. You are required to return the modified array.
#Note: The generated output is true if you modify the given array successfully.Otherwise false.
#Geeky Challenge: Solve this problem in O(n) time complexity.

class Solution:
    # Function to partition the array around the range [a, b]
    def threeWayPartition(self, array, a, b):
        n = len(array)
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            if array[mid] < a:
                # Case 1: Element is smaller than the range
                # Swap current element with the 'low' pointer
                array[low], array[mid] = array[mid], array[low]
                low += 1
                mid += 1
            elif array[mid] > b:
                # Case 2: Element is greater than the range
                # Swap current element with the 'high' pointer
                # Do NOT increment mid yet, as the swapped element 
                # from 'high' needs to be checked.
                array[mid], array[high] = array[high], array[mid]
                high -= 1
            else:
                # Case 3: Element is within the range [a, b]
                # Just move to the next element
                mid += 1
        
        # Note: The problem usually expects the array to be modified in-place.
        return array
