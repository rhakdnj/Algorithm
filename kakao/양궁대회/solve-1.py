from collections import deque


def bfs(n, info):
    res = []
    lion_info = 0, [0] * 11
    q = deque([lion_info])
    max_diff = 0

    while q:
        focus, lion_info = q.popleft()
        if sum(lion_info) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if info[i] == lion_info[i] == 0:
                    continue
                if info[i] >= lion_info[i]:
                    apeach += 10 - i
                else:
                    lion += 10 - i
            if apeach < lion:
                diff = lion - apeach
                if max_diff > diff:
                    continue
                if max_diff < diff:
                    max_diff = diff
                    res.clear()
                res.append(lion_info)
        elif sum(lion_info) > n:
            continue
        elif focus == 10:
            temp = lion_info[:]
            temp[focus] = n - sum(temp)
            q.append((-1, temp))
        else:
            temp1 = lion_info[:]
            temp1[focus] = info[focus] + 1
            q.append((focus + 1, temp1))
            temp2 = lion_info[:]
            temp2[focus] = 0
            q.append((focus + 1, temp2))

    return res


def solution(n, info):
    answer = bfs(n, info)

    if not answer:
        return [-1]
    elif len(answer) == 1:
        return answer[0]
    else:
        return answer[-1]


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
