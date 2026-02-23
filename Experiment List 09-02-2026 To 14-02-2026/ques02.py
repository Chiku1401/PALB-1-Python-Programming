'''Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. 
'''
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(current_sum, current_combination, start_index):
            if current_sum == target:
                
                result.append(list(current_combination))
                return
            if current_sum > target or start_index == len(candidates):
                return

            
            current_combination.append(candidates[start_index])
            backtrack(current_sum + candidates[start_index], current_combination, start_index)
            current_combination.pop() 

            backtrack(current_sum, current_combination, start_index + 1)

        backtrack(0, [], 0)
        return result
