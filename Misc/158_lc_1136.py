"""
Parallel Course (LC Premium) :

There are N courses, labelled from 1 to N.
We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.
In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.
Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

Example 1:

Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation:
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.


Example 2:

Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation:
No course can be studied because they depend on each other.


Note:

    1 <= N <= 5000
    1 <= relations.length <= 5000
    relations[i][0] != relations[i][1]
    There are no repeated relations in the input.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # create graph
        graph = defaultdict(list)

        # indegree of all nodes (1-based indexing)
        indegree = [0] * (n + 1)

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        # queue for nodes with indegree 0
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)

        if not queue:
            return -1

        step = 0
        visited_count = 0

        # BFS level by level
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                cur = queue.popleft()
                visited_count += 1
                for nxt in graph[cur]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)

        return step if visited_count == n else -1


if __name__ == "__main__":
    ins = Solution()
    print(ins.minimumSemesters(4, [[1, 3], [2, 3], [4, 2]]))
