#Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

def isPalinArray(arr):
    # Iterate through each number in the array
    for num in arr:
        # Convert to string and check against its reverse
        s = str(num)
        if s != s[::-1]:
            # If any number fails, the whole array fails
            return 0 # GFG often expects 0 for False
            
    # If all pass, return 1
    return 1 # GFG often expects 1 for True
