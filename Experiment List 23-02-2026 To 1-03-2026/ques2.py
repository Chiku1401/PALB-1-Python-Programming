"""
Min Add to Make Parentheses Valid.
"""

# Q2: Min Add to Make Parentheses Valid
class Solution:
    def minParentheses(self, s):
        open_needed = 0
        balance = 0
        
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ')'
                if balance > 0:
                    balance -= 1
                else:
                    open_needed += 1
        
        return open_needed + balance