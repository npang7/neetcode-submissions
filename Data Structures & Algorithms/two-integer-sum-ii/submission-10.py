class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,num in enumerate(numbers):
            j=i
            if j+1 < len(numbers): j = i+1
            if num + numbers[j] == target :
                return [i+1, j+1]
            while num + numbers[j] < target and j+1 < len(numbers):
                j += 1
                if num + numbers[j] == target:
                    return [i+1, j+1]
        return []