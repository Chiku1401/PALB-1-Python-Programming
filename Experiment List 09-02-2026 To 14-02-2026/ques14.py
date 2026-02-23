'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. 
If target is not found in the array, return [-1, -1]. 
You must write an algorithm with O(log n) runtime complexity
'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_pos

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_pos

        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = find_last(nums, target)
        return [first, last]

