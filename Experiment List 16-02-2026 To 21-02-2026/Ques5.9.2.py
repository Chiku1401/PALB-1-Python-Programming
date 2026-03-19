class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        
        # Step 1: Find pivot (smallest element index)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low
        
        # Binary search function to count <= x
        def count(arr, l, r, x):
            ans = l - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= x:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
        # Count in both sorted parts
        count1 = count(arr, 0, pivot - 1, x) if pivot > 0 else -1
        count2 = count(arr, pivot, n - 1, x)
        
        total = 0
        if count1 != -1:
            total += count1 + 1
        if count2 != pivot - 1:
            total += count2 - pivot + 1
        
        return total
