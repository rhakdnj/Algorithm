from typing import *
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순으로 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]


solution = Solution()
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
solution.findItinerary(tickets)
