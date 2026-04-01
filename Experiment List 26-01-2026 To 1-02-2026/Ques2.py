#You are given a string s consisting only of the characters '(' and ')'. Your task is to
#determine the minimum number of parentheses (either '(' or ')') that must be inserted at
#any positions to make the string s a valid parentheses string.

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