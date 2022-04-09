def solution(s):
    answer = 1000

    for n in range(1, len(s) // 2 + 2):
        res = ''
        cnt = 1
        temp = s[: n]
        for j in range(n, len(s) + n, n):
            if temp == s[j: j + n]:
                cnt += 1
            else:
                if cnt == 1:
                    res += temp
                else:
                    res += (str(cnt) + temp)
                cnt = 1
                temp = s[j: j + n]
        answer = min(answer, len(res))

    return answer
