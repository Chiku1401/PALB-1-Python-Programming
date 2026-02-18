#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.


class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If the array has only one element, we are already at the end
        if n <= 1:
            return 0
        
        # If the first element is 0, we can't move anywhere
        if arr[0] == 0:
            return -1
            
        max_reachable = arr[0]
        steps_left = arr[0]
        jumps = 1
        
        for i in range(1, n - 1):
            # Update the maximum distance we can reach
            max_reachable = max(max_reachable, i + arr[i])
            
            # Use a step to move to the current index
            steps_left -= 1
            
            # If no more steps are left in the current jump range
            if steps_left == 0:
                jumps += 1
                
                # If the current index is the furthest we can go, we're stuck
                if i >= max_reachable:
                    return -1
                
                # Refresh steps for the next jump
                steps_left = max_reachable - i
                
        return jumps
