class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 总油量不足，任何起点都不可能成功
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            # 在站 i 加油，再开往下一站后的剩余油量
            tank += gas[i] - cost[i]

            if tank < 0:
                # start 到 i 都不能作为起点，下一次从 i + 1 尝试
                start = i + 1
                tank = 0

        return start



# i：现在检查哪里
# tank：当前这次尝试剩多少油
# start：当前这次尝试是从哪里开始的