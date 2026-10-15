from collections import deque
class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:

        next_courses = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # 建立先修课指向后续课的关系
        for course, prereq in prerequisites:
            next_courses[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        # 所有没有未完成先修课的课程，先加入队列
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            course = queue.popleft()

            # 当前课程可以完成，记录到修课顺序中
            order.append(course)

            # 更新依赖当前课程的后续课程
            for next_course in next_courses[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # 必须包含全部课程，才是完整的合法顺序
        if len(order) == numCourses:
            return order

        return []

#只需要返回任意一种合法顺序，不需要返回所有可能的顺序。