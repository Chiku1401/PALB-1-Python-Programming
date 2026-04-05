"""
Score of Parentheses String.
"""

# Q3: Score of Parentheses
class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack.pop()
                if val == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * val
        
        return stack[0]
