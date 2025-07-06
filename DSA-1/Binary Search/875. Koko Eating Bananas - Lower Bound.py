import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l)//2

            totaltime = 0
            for b in piles:
                totaltime += math.ceil(b/m)
            
            if totaltime > h:
                l = m+1
            elif totaltime <= h:
                r = m

        return l