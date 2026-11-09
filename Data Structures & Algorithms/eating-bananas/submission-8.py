class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            k = (left+right)//2
            time = 0 
            for pile in piles:
                time += math.ceil(pile/k)
            if time <= h :
                right = k
            else:
                left = k+1

        return left
            
