class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # in_start = newInterval[0]
        # in_end = newInterval[1]
        for i in range(len(intervals)):
            current = intervals[i]

            #current完全在左边，直接把current加入res
            if current[1] < newInterval[0]: 
                res.append(current)
            #current完全在右边，先加入newInterval，再加剩下的，return
            elif current[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else: #有重叠，更新newInterval，也许后续还要merge
                left = min(current[0],newInterval[0])
                right = max(current[1],newInterval[1])
                newInterval = [left,right]

        #循环结束都没有遇到“完全在右边”的区间，需要手动加入
        res.append(newInterval)#别忘记！

        return res



