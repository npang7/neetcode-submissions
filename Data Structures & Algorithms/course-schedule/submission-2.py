from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1.建立数组
        next_courses = [[] for _ in range(numCourses)] # 每门课对应的后续课程
        indegree = [0] * numCourses # 每门课还有多少门先修课没有完成
        # 建立课程之间的依赖关系：indegree\next_courses
        for course, prereq in prerequisites:
            next_courses[prereq].append(course)
            indegree[course] += 1

        queue = deque() #记录现在可以修的课程
        # 2. 没有先修要求的课程，可以先修，加入queue
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            # 当前课程完成，更新后续课程的先修要求
            for next_course in next_courses[course]: 
                #把要求这门课作为先修的课程的indegree降低
                indegree[next_course] -= 1
                # 所有先修课都完成了，就可以修这门课
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses

# 就在题干这句话里：
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# 意思是：
# 一共有 numCourses 门课程，编号从 0 到 numCourses - 1

# 中文思路清单（拓扑排序：入度数组 + 队列）
#
# 1. 理解课程编号和先修关系。
#    - 题目规定课程编号为 0 到 numCourses - 1。
#    - 因此，我们让数组下标直接对应课程编号。
#    - prerequisites 中的 [a, b] 表示：先完成 b，才能修 a。
#    - 建图方向是 b 指向 a，也就是先修课指向后续课。
#
# 2. 初始化后续课程列表和入度数组。
#    - next_courses = [[] for _ in range(numCourses)]。
#    - next_courses[i]：哪些课程把课程 i 作为先修课。
#    - indegree = [0] * numCourses。
#    - indegree[i]：课程 i 还有多少门先修课没有完成。
#    - course 是课程编号，indegree[course] 才是这门课的入度。
#
# 3. 遍历 prerequisites，建立依赖关系。
#    - for course, prereq in prerequisites：
#      course 是后续课程，prereq 是它的先修课程。
#    - next_courses[prereq].append(course)：
#      记录完成 prereq 后，需要更新 course 的先修要求。
#    - indegree[course] += 1：
#      course 多了一门需要先完成的课程。
#
# 4. 创建队列，把所有入度为 0 的课程加入队列。
#    - 使用 for course in range(numCourses)，检查全部课程编号。
#    - 如果 indegree[course] == 0，就执行 queue.append(course)。
#    - 队列保存当前已经满足所有先修要求、可以修的课程。
#    - 没有出现在 prerequisites 中的课程也要检查和完成。
#    - 入度为 0 的课程可能有多门，要全部加入队列。
#
# 5. 初始化 completed = 0，然后开始处理队列。
#    - completed 表示已经完成的课程数量。
#    - 只要队列不为空，就执行 course = queue.popleft()。
#    - 取出的课程已经满足先修要求，可以视为完成。
#    - 执行 completed += 1。
#
# 6. 更新所有依赖当前课程的后续课程。
#    - 遍历 next_courses[course]，逐个得到 next_course。
#    - 执行 indegree[next_course] -= 1。
#    - 当前课程已经完成，所以后续课程少了一门未完成的先修课。
#    - 只有当 indegree[next_course] == 0 时，才把它加入队列。
#    - 如果入度仍然大于 0，说明还有其他先修课没完成，必须继续等待。
#
# 7. 队列为空时，检查是否完成全部课程。
#    - 返回 completed == numCourses。
#    - 相等：所有课程都能完成，返回 True。
#    - 不相等：剩下的课程被循环依赖卡住，返回 False。
#    - 即使能完成一部分课程，只要无法完成全部课程，也要返回 False。
#
# 8. 容易混淆的地方。
#    - [a, b] 是先修 b 再修 a，不能把依赖方向看反。
#    - next_courses[i] 保存后续课程，不是课程 i 的先修课程。
#    - indegree[i] 会随着课程完成而减少，不是始终保持初始值。
#    - 课程入队时，必须已经满足全部先修要求。
#    - 完成一门先修课，不一定就能解锁后续课程。
#      例如一门课需要两门先修课，必须把入度从 2 减到 0 才能入队。
#    - 不需要额外的 visited 集合。
#      每门课只在入度变成 0 时入队；初始入度为 0 的课程在初始化时入队。
#    - 这里不需要按层处理队列，因为题目只判断能否完成，不计算时间。
#    - 如果 prerequisites 为空，所有课程初始入度都是 0，最终返回 True。
#
# 9. 时间和空间复杂度。
#    - V = numCourses：课程数量。
#    - E = len(prerequisites)：先修关系数量。
#    - 时间复杂度：O(V + E)。
#      初始化并检查所有课程，每门课最多出队一次，
#      每条先修关系最多处理一次。
#    - 空间复杂度：O(V + E)。
#      后续课程列表需要 O(V + E)，入度数组和队列需要 O(V)。
#
# 快速记忆思路
# 建后续课程表、统计入度 → 零入度课程入队。
# 出队算完成 → 后续课程入度减一 → 减到零就入队。
# 最后检查：完成数量是否等于总课程数量。
#
# 口语讲述思路
#
# I'll use topological sort with a queue.
#
# For each pair [a, b], course b must be completed before course a.
# I add an edge from b to a and increase the indegree of a.
# The indegree represents how many prerequisites are still unfinished.
#
# I also keep a list of the courses that depend on each course.
# This lets me update them when a prerequisite is completed.
#
# First, I add all courses with an indegree of zero to the queue.
# These courses can be taken immediately.
#
# While the queue is not empty, I remove a course
# and increase the completed course count.
#
# Then I go through the courses that depend on it
# and decrease their indegrees by one.
# If a course's indegree becomes zero, all its prerequisites are complete,
# so I add it to the queue.
#
# When the queue becomes empty, I compare the completed count
# with the total number of courses.
# If they are equal, I return true.
# Otherwise, a cycle prevents some courses from being completed,
# so I return false.
#
# The time complexity is O(V + E),
# where V is the number of courses and E is the number of prerequisite pairs.
# The space complexity is also O(V + E)
# for the adjacency lists, the indegree array, and the queue.