from collections import deque


def get_adjacent(cur, words):
    for word in words:
        cnt = 0
        for c, w in zip(cur, word):
            if c != w:
                cnt += 1

        if cnt == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        cur = queue.popleft()

        for next_word in get_adjacent(cur, words):
            if next_word not in dist:
                dist[next_word] = dist[cur] + 1
                queue.append(next_word)

    return dist.get(target, 0)


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
