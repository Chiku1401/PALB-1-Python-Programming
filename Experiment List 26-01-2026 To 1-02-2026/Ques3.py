#Given a string s consisting of balanced parentheses, calculate the score of the string based on the following rules:
#"O" has a score of 1.
#"AB" has a score of A + B, where A and B are balanced parentheses strings.
#'(A)" has a score of 2 × score(A), where A is a balanced parentheses string.


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
