from typing import *
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i) -> bool:
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    numCourses = 3
    prerequisites = [[1, 2], [0, 1], [0, 2]]
    solution.canFinish(numCourses, prerequisites)