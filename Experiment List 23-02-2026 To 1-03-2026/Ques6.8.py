# Lexicographically Largest String After K Deletions

class Solution:
    def maxSubseq(self, s, k):
        stack = []
        
        for ch in s:
            while k > 0 and stack and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # If deletions still remain
        if k > 0:
            stack = stack[:-k]
        
        return ''.join(stack)