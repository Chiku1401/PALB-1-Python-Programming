#Given an array arr[] denoting heights of n towers and a positive integer k.
#For each tower, you must perform exactly one of the following operations exactly once.
#Increase the height of the tower by k
#Decrease the height of the tower by k
#Find out the minimum possible difference between the height of the shortest and tallest towers
#after you have modified each tower.
#You can find a slight modification of the problem here.
#Note: It is compulsory to increase or decrease the height by k for each tower. After the operation,the resultant array should not contain any negative integers.


class Solution:
    def getMinDiff(self, arr, n, k):
        if n == 1:
            return 0
            
        # 1. Sort the array
        arr.sort()
        
        # 2. Initial difference
        ans = arr[n-1] - arr[0]
        
        # 3. Traverse through the array to find the best split point
        for i in range(1, n):
            # Skip if decreasing the height results in a negative value
            if arr[i] - k < 0:
                continue
            
            # Potential smallest height
            # Either the first tower + k OR the current tower - k
            temp_min = min(arr[0] + k, arr[i] - k)
            
            # Potential largest height
            # Either the last tower - k OR the previous tower + k
            temp_max = max(arr[n-1] - k, arr[i-1] + k)
            
            # Update the answer with the minimum difference found
            ans = min(ans, temp_max - temp_min)
            
        return ans
