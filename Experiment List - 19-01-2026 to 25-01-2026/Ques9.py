#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the value and its corresponding index
        prev_map = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                # If the difference exists in our map, we found the pair
                return [prev_map[diff], i]
            # Otherwise, add the current number and its index to the map
            prev_map[n] = i
