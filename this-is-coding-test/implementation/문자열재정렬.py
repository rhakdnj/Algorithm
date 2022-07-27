# Facebook 인터뷰
# 문자열 재정렬
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(s: str) -> None:
    answer = []
    summary = 0
    for i in range(len(s)):
        if s[i].isdigit():
            summary += int(s[i])
        else:
            answer.append(s[i])

    if summary != 0:
        answer.append(str(summary))

    print(''.join(answer))


n = input()
solution(n)
