def solution(s):
    answer = len(s)

    for k in range(1, int(len(s) / 2) + 1):
        pos = 0
        length = len(s)

        while pos + k <= len(s):
            unit = s[pos: pos + k]
            pos += k

            cnt = 0
            while pos + k <= len(s):
                if s[pos: pos + k] == unit:
                    cnt += 1
                    pos += k
                else:
                    break
            if cnt > 0:
                length -= k * cnt
                if cnt < 9:
                    length += 1
                elif cnt < 99:
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4
        answer = min(answer, length)

    return answer


print(solution("xababcdcdababcdcd"))
