class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # in_start = newInterval[0]
        # in_end = newInterval[1]
        for i in range(len(intervals)):
            current = intervals[i]

            #current完全在左边
            if current[1] < newInterval[0]: 
                res.append(current)
            #current完全在右边
            elif current[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                left = min(current[0],newInterval[0])
                right = max(current[1],newInterval[1])
                newInterval = [left,right]
        res.append(newInterval)
        return res



