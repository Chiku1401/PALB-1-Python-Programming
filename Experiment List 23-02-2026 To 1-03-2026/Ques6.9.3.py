# Balancing Consonants and Vowels Ratio

class Solution:
    def countBalanced(self, arr):
        vowels = set('aeiou')
        
        prefix = 0
        freq = {0: 1}
        result = 0
        
        for word in arr:
            diff = 0
            for ch in word:
                if ch in vowels:
                    diff += 1
                else:
                    diff -= 1
            
            prefix += diff
            
            if prefix in freq:
                result += freq[prefix]
                freq[prefix] += 1
            else:
                freq[prefix] = 1
        
        return result