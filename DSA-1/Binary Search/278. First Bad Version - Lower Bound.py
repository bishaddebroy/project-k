# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            m = l + (r-l)//2
            b = isBadVersion(m)

            if b == True:
                r = m
            else:
                l = m + 1
        
        return l