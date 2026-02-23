'''Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.Each number in candidates may only be used once in the combination
'''
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort() 
        
        def backtrack(idx, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return
            
            for i in range(idx, len(candidates)):
                
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target - current_sum:
                    break
                    
                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
