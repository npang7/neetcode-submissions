class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = {}
        for num in nums:
            count[num] = count.get(num , 0) +1
        arr = []
        for num,cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        for i in range(0,k):
            output.append(arr.pop()[1])
        return output