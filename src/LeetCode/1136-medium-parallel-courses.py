# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.
#
# In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.
#
# Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.
#
#
#
# Example 1:
#
#
# Input: n = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 1 and 2.
# In the second semester, you can take course 3.
# Example 2:
#
#
# Input: n = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: No course can be studied because they are prerequisites of each other.
#
#
# Constraints:
#
# 1 <= n <= 5000
# 1 <= relations.length <= 5000
# relations[i].length == 2
# 1 <= prevCoursei, nextCoursei <= n
# prevCoursei != nextCoursei
# All the pairs [prevCoursei, nextCoursei] are unique.

from typing import Dict, List
import collections


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        in_degree: Dict[int, int] = collections.defaultdict(int)
        for prev, next in relations:
            adj_list[prev].append(next)
            in_degree[next] += 1
        queue = collections.deque([i for i in range(1, n + 1) if i not in in_degree])
        completed = set()
        semesters = 0
        while queue:
            next_semester_load = len(queue)
            for _ in range(next_semester_load):
                course = queue.popleft()
                for next_course in adj_list[course]:
                    if next_course not in completed:
                        in_degree[next_course] -= 1
                        if in_degree[next_course] == 0:
                            queue.append(next_course)
                completed.add(course)
            semesters += 1

        return semesters if len(completed) == n else -1


solution = Solution()
print(solution.minimumSemesters(n=3, relations=[[1, 3], [2, 3]]))
print(solution.minimumSemesters(n=3, relations=[[1, 2], [2, 3], [3, 1]]))
print(solution.minimumSemesters(n=3, relations=[]))
