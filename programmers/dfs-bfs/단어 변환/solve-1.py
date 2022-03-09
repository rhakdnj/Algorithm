from collections import deque


def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])
    visited = [0 for _ in range(len(words))]

    while queue:
        word, cnt = queue.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    queue.append([words[i], cnt + 1])
                    visited[i] = True
    return answer
