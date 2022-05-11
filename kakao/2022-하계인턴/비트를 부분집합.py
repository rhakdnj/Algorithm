from bisect import bisect_left


def solution(info: str, query: str):
    answer = []
    dic = {'-': 0, 'cpp': 1, 'java': 2, 'python': 3,
           'backend': 1, 'frontend': 2,
           'junior': 1, 'senior': 2,
           'chicken': 1, 'pizza': 2}
    score_list = [[] for _ in range(4 * 3 * 3 * 3)]

    for s in info:
        s = s.split()
        arr = (dic[s[0]] * 3 * 3 * 3,
               dic[s[1]] * 3 * 3,
               dic[s[2]] * 3,
               dic[s[3]])
        score = int(s[4])

        for i in range(1 << 4):
            idx = 0
            for j in range(4):
                if i & (1 << j):
                    idx += arr[j]
            score_list[idx].append(score)

    for i in range(4 * 3 * 3 * 3):
        score_list[i].sort()

    for q in query:
        q = q.split()
        idx = (dic[q[0]] * 3 * 3 * 3 + dic[q[2]] * 3 * 3 + dic[q[4]] * 3 + dic[q[6]])
        answer.append(len(score_list[idx]) - bisect_left(score_list[idx], int(q[7])))
    return answer