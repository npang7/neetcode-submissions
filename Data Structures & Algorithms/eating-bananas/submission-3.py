class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        #totaltime=0 错误的位置！
        while left < right:
            k = (left+right)//2
            totaltime=0  #是在每次while循环内部清零
            for pile in piles:
                totaltime += math.ceil(pile/k)
            if totaltime <= h :
                right = k
            else:
                left = k + 1
        return left
        
# ① 外层循环：O(log m) 次。 搜索的速度范围是 1 到 m。每次检查中间速度后，搜索范围大约减半。例如范围有 1000 个速度，大约检查 10 次就够了，因为 2¹⁰ = 1024。
# ② 每次检查：O(n)。 对一个候选速度 k，必须遍历所有 n 堆，计算总共需要多少小时。