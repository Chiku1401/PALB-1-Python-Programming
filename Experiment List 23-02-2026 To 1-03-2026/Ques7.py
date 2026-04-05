#Given three sorted arrays in non-decreasing order, print all common elements
#in non-decreasing order across these arrays. If there are no such elements return
#an empty array. In this case, the output will be -1.
#Note: can you handle the duplicates without using any additional Data Structure?

class Solution:
    def commonElements(self, A, B, C):
        # Infer lengths since the driver isn't passing them anymore
        n1, n2, n3 = len(A), len(B), len(C)
        i, j, k = 0, 0, 0
        res = []
        
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] == C[k]:
                res.append(A[i])
                common_val = A[i]
                # Skip all identical elements in all arrays to avoid duplicates
                while i < n1 and A[i] == common_val: i += 1
                while j < n2 and B[j] == common_val: j += 1
                while k < n3 and C[k] == common_val: k += 1
            
            # Move the pointer of the smallest element
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
                
        return res
