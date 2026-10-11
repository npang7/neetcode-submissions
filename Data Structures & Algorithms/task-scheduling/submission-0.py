import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 统计每种任务需要执行多少次
        task_counts = Counter(tasks)   #得到dictionary
        # 保存次数的负数，优先取出剩余次数最多的任务
        heap = []
        for count in task_counts.values():
            heap.append(-count)
        heapq.heapify(heap)

        # 保存：(剩余次数的负数, 可以再次执行的时间)
        cooldown = deque() #往右边加入记录，从左边取出记录
        time = 0

        # 还有可以执行或正在冷却的任务，就继续
        while heap or cooldown:
            time += 1

            # 当前周期开始时，让冷却结束的任务重新可用
            while cooldown and cooldown[0][1] <= time:
                count, ready_time = cooldown.popleft()
                heapq.heappush(heap, count)

            if heap:
                # 执行一次任务，让剩余次数减少一次
                remaining = heapq.heappop(heap) + 1

                # 还有剩余任务，就进入冷却状态
                if remaining < 0:
                    ready_time = time + n + 1 #不要忘记加1！
                    cooldown.append((remaining, ready_time))
            # 如果 heap 为空，这个周期就空闲等待
        return time
        


# 思路是：模拟每一个周期，用堆选择任务，用队列管理冷却。
# 容器	     保存什么
# heap	     当前可以执行的任务的剩余次数
# cooldown	 正在冷却的任务的剩余次数，以及何时能再次执行


# 每个周期：
# 1. 把冷却结束的任务放回堆。
# 2. 如果堆不为空，执行剩余次数最多的任务。
# 3. 如果这个任务还没全部完成，就让它进入冷却队列。
# 4. 如果堆为空，这个周期就是 idle。
# 优先执行剩余次数多的任务，可以早点开始它们的冷却，减少最后只剩一种任务时的等待。