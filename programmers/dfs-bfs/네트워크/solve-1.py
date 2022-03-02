def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    # 같은 네트워크에 있는 노드는 같은 숫자로 치환
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))
