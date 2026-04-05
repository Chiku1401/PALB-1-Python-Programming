#You are given two binary strings s1 and s2 of equal length, and the task is to find
#the minimum number of swaps required to make them identical. The only allowed
#operation is swapping characters between the two strings (i.e., you can
#swap s1[i] with s2[j], but not within the same string). If it is impossible to make the two
#strings equal through such swaps, return -1.


class Solution:
    def minSwaps(self, s1, s2):
        xy = 0  # s1[i] = 0, s2[i] = 1
        yx = 0  # s1[i] = 1, s2[i] = 0
        
        for i in range(len(s1)):
            if s1[i] == '0' and s2[i] == '1':
                xy += 1
            elif s1[i] == '1' and s2[i] == '0':
                yx += 1
        
        # If total mismatches is odd → impossible
        if (xy + yx) % 2 != 0:
            return -1
        
        # Swaps calculation
        return (xy // 2) + (yx // 2) + 2 * (xy % 2)
