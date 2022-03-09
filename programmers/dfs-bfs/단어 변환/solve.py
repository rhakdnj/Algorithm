def dfs(begin, target, words, visited):
    cnt = 0
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth

        for i in range(len(words)):
            if visited[i]:
                continue
            cnt = 0
            for a, b in zip(cur, words[i]):
                if a != b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth + 1))


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [False] * len(words)
    answer = dfs(begin, target, words, visited)
    return answer

