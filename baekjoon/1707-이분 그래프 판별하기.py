import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def solution(v, e):
    graph = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    set_ = [0 for _ in range(v + 1)]

    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    is_bipartite = True

    def BFS(start_node):
        nonlocal is_bipartite
        dq = deque()
        dq.append(start_node)
        visited[start_node] = True

        while dq:
            curr = dq.popleft()
            next_: int
            for next_ in graph[curr]:
                if not visited[next_]:
                    dq.append(next_)
                    visited[next_] = True
                    set_[next_] = (set_[curr] + 1) % 2
                elif set_[next_] == set_[curr]:
                    is_bipartite = False
                    return

    for i in range(1, v + 1):
        if is_bipartite:
            BFS(i)
        else:
            print("NO")
            return

    print("YES")
    return


if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        solution(*map(int, input().split()))

"""
노드의 집합을 2개로 나누는데, 인접한 노드끼리 집합이 되지 않도록 적절하게 임의로 분할할 수 있다고 합니다.
잘 생각해 보면 트리의 경우에는 항상 이분 그래프가 된다는 것을 알 수 있습니다.

사이클이 발생하지 않으면 탐색을 하면서 다음 노드를 이번 노드와 다른 집합으로 지정하면 되기 때문입니다.
단, 사이클이 발생했을 때는 이런 이분 그래프가 불가능할 때가 있습니다.

다른 집합 노드가 탐색한 노드에 다시 접근하게 됐을 때 
현재 노드의 집합과 같으면 이분 그래프가 불가능하다는 것으로 판별할 수 있다.

1. visited 배열에서 True, False로 해결하려고하면 안되는 이유는 
    - 방향성 그래프에서는 해결이 안된다. 들어 오는 edge에 대해 해결할 수 없다.
2. 이분 그래프 접합 배열을 따로 둔다.
"""
