"""
Combination Sum III
"""

class Solution:
    def combinationSum(self, n, k):
        # GeeksforGeeks passes (target sum 'n', number of elements 'k')
        result = []
        
        def backtrack(start_num, current_comb, current_sum):
            # Base Case 1: We have exactly 'k' elements
            if len(current_comb) == k:
                # If the sum perfectly matches 'n', it's a valid combination
                if current_sum == n:
                    result.append(list(current_comb))
                return
            
            # Pruning: If our sum exceeds 'n', stop exploring this path
            if current_sum > n:
                return
                
            # Explore adding numbers from 'start_num' up to 9
            for i in range(start_num, 10):
                current_comb.append(i)
                # Recurse with the next number (i + 1) to avoid duplicates
                backtrack(i + 1, current_comb, current_sum + i)
                # Backtrack: remove the number we just added and try the next 'i'
                current_comb.pop()

        # Start backtracking from number 1, with an empty combination and sum of 0
        backtrack(1, [], 0)
        return result
