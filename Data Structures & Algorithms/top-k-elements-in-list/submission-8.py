class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        x = len(nums) + 1
        freq = [[]for i in range(x)]

        for num, cnt in count.items():
            freq[cnt].append(num) #注意不是：freq[cnt] = num,因为可能有多个num是同一个cnt
        
        arr = []
        for i in range(len(nums), 0, -1):
            for n in freq[i] :
                arr.append(n)
                if len(arr) == k :
                    return arr
   