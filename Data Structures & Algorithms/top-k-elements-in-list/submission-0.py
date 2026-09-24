class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = {}
        for num in nums:
            count[num]=count.get(num, 0) + 1
        for i in range(0,k) :
                max_key = max(count, key = count.get)
                output.append(max_key)
                del count[max_key]

        return output
