"""
Lexicographically largest string after k deletions.
"""

# Q10: Lexicographically largest after k deletions
class Solution:
    def maxSubseq(self, s, k):
        stack = []
        
        for ch in s:
            while k > 0 and stack and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        return ''.join(stack[:len(stack)-k])
