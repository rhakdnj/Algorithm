import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def solution(a, b, c):
    answer = [False for _ in range(201)]
    visited = [[False for _ in range(201)] for _ in range(201)]
    cases = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))
    limits = (a, b, c)

    def BFS():
        dq = deque()
        dq.append((0, 0))
        visited[0][0] = True
        answer[limits[2]] = True

        while dq:
            curr = dq.popleft()
            a, b, c = curr[0], curr[1], limits[2] - (curr[0] + curr[1])

            for case in cases:
                # 리스트 복제
                next = [a, b, c]

                start, end = case[0], case[1]
                next[end] += next[start]
                next[start] = 0

                # 물이 넘치는 경우
                if next[end] > limits[end]:
                    next[end], next[start] = limits[end], next[end] - limits[end],

                if not visited[next[0]][next[1]]:
                    visited[next[0]][next[1]] = True
                    dq.append((next[0], next[1]))

                    # A의 물의 양이 0일 때 C의 물 무게를 추가
                    if next[0] == 0:
                        answer[next[2]] = True

    BFS()
    for i in range(201):
        if answer[i]:
            print(i, end=' ')


if __name__ == '__main__':
    solution(*map(int, input().split()))

"""
각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다. 

처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다. 

이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데, 
이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다. 



이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다. 
첫 번째 물통(용량이 A인)이 비어 있을 때, 
세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.

지금까지 접해 봤던 그래프 데이터를 저장하고 저장한 자료구조를 이용하는 방식과 달리,
그래프 원리를 적용해 그래프를 역으로 그리는 방식으로 접근하는 문제입니다. A, B, C의 특정 무게 상태를 
1개의 노드로 가정하고, 조건에 따라 이 상태에서 변경할 수 있는 이후 무게 상태가 에지로 이어진 인접한 
노드라고 생각하고, 문제를 접근해 봅니다.

A, B는 비어 있고 C는 꽉 차 있으므로 최초 출발 노드를 (0, 0, 3번째 물통의 용량)

노드에서 갈 수 있는 6개의 경우
(A -> B, A -> C, B -> A, B -> C, C -> A, C -> B)에 관해
다음 노드로 정해 큐에 추가한다.

보내는 물통의 모든 용량을 받는 물통에 저장하고, 보내는 물통에는 0을 저장한다.
단, 받는 물동이 넘칠 때는 초과하는 값만큼 보내는 물통에 남긴다.

큐에 추가하는 시점에 1번째 물통(A)의 무게가 0일 때가 있으면 3번 째 물통(C)의 값을 정답 리스트에 추가한다.
"""
