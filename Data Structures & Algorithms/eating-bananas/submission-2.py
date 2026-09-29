class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            k = (left+right)//2
            totaltime=0
            for pile in piles:
                totaltime += math.ceil(pile/k)
            if totaltime <= h :
                right = k
            else:
                left = k + 1
        return left
                