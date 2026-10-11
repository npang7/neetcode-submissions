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
                heapq.heappush(heap, count) #把它放回保存“可执行任务”的堆里

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


# Task Scheduler — 思路清单
#
# 1. 理解题意：
#    - 每个周期最多执行一个任务。
#    - 任务可以重新排列。
#    - 相同任务之间至少间隔 n 个周期。
#    - 无任务可执行时，需要 idle，idle 也计入时间。
#    - 返回完成所有任务需要的最少周期数。
#
# 2. 贪心选择：
#    - 每次优先执行当前可用、且剩余次数最多的任务。
#    - 尽早开始频繁任务的冷却，减少末尾的等待。
#
# 3. 统计次数：
#    - 使用 Counter(tasks) 统计每种任务的出现次数。
#
# 4. 建立堆：
#    - heap 保存当前可以执行的任务的剩余次数。
#    - 将次数存成负数，用最小堆模拟最大堆。
#    - 每个堆元素代表一种任务，即使次数相同也分别保存。
#
# 5. 建立冷却队列：
#    - cooldown 保存正在冷却的任务。
#    - 每条记录是 (剩余次数的负数, 可再次执行的时间)。
#    - 所有任务冷却长度相同，因此记录按可执行时间递增。
#
# 6. 开始模拟：
#    - time 从 0 开始。
#    - while heap or cooldown：还有未完成任务，就继续。
#    - 每次循环先执行 time += 1，进入下一个周期。
#
# 7. 先处理冷却结束：
#    - 如果队首任务的可执行时间 <= time：
#      从 cooldown 中取出，并将剩余次数放回 heap。
#    - 放回 heap 表示现在可以执行，尚未实际执行。
#
# 8. 再执行任务：
#    - 如果 heap 非空，取出剩余次数最多的任务。
#    - 负数次数加一，表示实际剩余次数减一。
#
# 9. 执行后判断：
#    - remaining == 0：全部完成，不再保存。
#    - remaining < 0：还有剩余，进入冷却队列。
#    - 下一次可执行时间 = time + n + 1。
#
# 10. 处理 idle：
#     - 如果 heap 为空，本周期不执行任务。
#     - time 已经增加，所以 idle 会自动计入总时间。
#
# 11. 结束条件：
#     - heap 和 cooldown 都为空，所有任务完成。
#     - 返回 time。
#
# 12. 复杂度：
#     - N：任务总数。
#     - m：任务种类数，最多 26。
#     - T：总周期数，包含 idle。
#     - 时间：O(T + N log m)。
#     - 额外空间：O(m)。
#     - 逐周期模拟时，时间分析需要包含 idle 周期。




# I first count how many times each task appears.

# I use a max heap to choose the available task with the most remaining
# executions. In Python, I simulate the max heap by storing negative counts.
# I also use a queue to track tasks that are cooling down.

# At the beginning of each CPU cycle, I move any tasks whose cooldown has
# finished back into the heap. Then I execute the available task with the
# highest remaining count.

# If that task still has executions left, I put it into the cooldown queue.
# Its next available time is the current time plus n plus one, because
# there must be n full cycles between two identical tasks.

# If no task is available, the current cycle is idle.

# I continue until both the heap and the cooldown queue are empty, and
# return the total number of cycles.

# heapq.heappush(heap, value) 做这两件事：
# 1. 插入：把新数字放到列表末尾。
# 2. 调整：如果新数字比父节点小，就向上移动，直到父节点不大于它，或者它已经到达堆顶。