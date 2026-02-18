#You are given two arrays a[] and b[], return the Union of both the arrays in any order. The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.



class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        # 1. Create a set from array 'a' to get unique elements
        # 2. Update it with elements from array 'b'
        # 3. Converting to a set automatically handles duplicates
        union_set = set(a).union(set(b))
        
        # Return the result as a list
        return list(union_set)
