#Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in
#sorted order without using any extra space. Modify a[] so that it contains the first n elements and
#modify b[] so that it contains the last m elements.

from collections import Counter

class Solution:
    def frequencySort(self, s):
        freq = Counter(s)
        unique_chars = list(freq.keys())
        unique_chars.sort(key=lambda x: (freq[x], x))
        
        res = []
        for char in unique_chars:
            res.append(char * freq[char])
            
        return "".join(res)