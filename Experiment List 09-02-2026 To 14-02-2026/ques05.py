'''Given an array of strings strs, group the anagrams together. You can return the answer in any order. 
  
Example 1: 
Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]] Explanation: 
•	There is no string in strs that can be rearranged to form "bat". 
•	The strings "nat" and "tan" are anagrams as they can be rearranged to form each other. 
•	The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other. 
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagrams_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            
            
            if sorted_word not in anagrams_map:
                anagrams_map[sorted_word] = []
            
            
            anagrams_map[sorted_word].append(word)

        
        return list(anagrams_map.values())
