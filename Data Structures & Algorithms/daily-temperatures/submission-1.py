class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #store the indices
        result = [0]* len(temperatures)
        for today in range(len(temperatures)):
            while stack and temperatures[today] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = today - prev_day
            stack.append(today)
        return result