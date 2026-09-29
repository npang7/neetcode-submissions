class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # 存还没找到更暖一天的日期下标

        for today in range(len(temperatures)):
            while stack and temperatures[today] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                result[previous_day] = today - previous_day

            stack.append(today)

        return result

# I use a stack to store indices for days that are still waiting for a warmer day.
# I also initialize a result array with zeros, one for each day.
# I go through the temperatures from left to right. While today’s temperature is higher than "the previous day's temperature whose the index" is on top of the stack, I pop that index. Today is the first warmer day for that earlier day, so I store the difference between their indices in the result array.
# After the while loop, I push today’s index onto the stack. The stack holds days that are still waiting for a warmer day. From bottom to top, the temperatures never go up. If a day is still in the stack at the end, its answer is zero.
# Each index is pushed and popped at most once, so the algorithm takes O(n) time and O(n) space.
# I use a stack to store the indices of days that are still waiting for a warmer day. I initialize a result array with one zero for each day.
# Then I go through the temperatures from left to right. While today’s temperature is higher than the temperature of the day on top of the stack, I pop that day’s index. I calculate how many days it waited and store that number in the result array.
# After the while loop, I push today’s index onto the stack. At the end, any day still in the stack keeps its answer of zero, and I return the result array.