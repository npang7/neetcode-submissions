from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 每门课对应的后续课程
        next_courses = [[] for _ in range(numCourses)]
        # 每门课还有多少门先修课没有完成
        indegree = [0] * numCourses

        # 建立课程之间的依赖关系
        for course, prereq in prerequisites:
            next_courses[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        # 没有先修要求的课程，可以先修
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1

            # 当前课程完成，更新后续课程的先修要求
            for next_course in next_courses[course]:
                indegree[next_course] -= 1

                # 所有先修课都完成了，就可以修这门课
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses