#Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.
#Return true if such a triplet exists, otherwise, return false.

class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == target:
                    return True
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return False
