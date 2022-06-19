"""
이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다.
데이터를 삭제하는 연산은 또 두 가지로 구분되는데
하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다.
"""

import sys
from heapq import heappop, heappush


def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    visited = [False] * k  # 인덱스 -> 입력의 순서, True, False -> 의미 있는지

    for j in range(k):
        cmd, num = input().split()

        if cmd == 'I':
            heappush(min_heap, (int(num), j))
            heappush(max_heap, (-int(num), j))
            visited[j] = True
        else:
            if num == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)

    if not min_heap and not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
