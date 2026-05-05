import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1

        while lo < hi:
            mid = (hi + lo) // 2
            hour_count = 0
            for pile in piles:
                hour_count += math.ceil(pile / mid)
            if hour_count > h:
                lo = mid + 1
            else:
                hi = mid 
            
        return lo
