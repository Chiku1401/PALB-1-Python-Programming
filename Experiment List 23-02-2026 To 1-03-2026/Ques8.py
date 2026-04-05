#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

class Solution:
    def factorial(self, N):
        res = 1
        # Calculate the factorial using simple multiplication
        # Python handles the large number logic automatically
        for i in range(2, N + 1):
            res *= i
        
        # The problem asks for a list of integers denoting the digits
        # Example: 120 -> [1, 2, 0]
        # We convert to string and then each character back to int
        return [int(d) for d in str(res)]
