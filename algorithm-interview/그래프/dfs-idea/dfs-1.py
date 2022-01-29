from typing import *

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(v, discovered=[]) -> List[int]:
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


print(f'recursive dfs: {recursive_dfs(1)}')
