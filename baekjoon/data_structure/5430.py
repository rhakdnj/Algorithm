# https://www.acmicpc.net/problem/5430
# AC

"""
R : Reverse 뒤집기
D : Drop 첫 번째 수를 버림

"""
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def solution(t: int) -> None:
    for _ in range(t):
        p = input()
        n = int(input())
        dq = deque(input()[1: -1].split(',') if n != 0 else [])

        r_cnt = 0
        for func in p:
            if func == 'R':
                r_cnt += 1
            else:
                if not dq:
                    print("error")
                    break
                if r_cnt % 2:
                    dq.pop()
                else:
                    dq.popleft()
        else:
            if r_cnt % 2:
                print("[" + ",".join(reversed(dq)) + "]")
            else:
                print("[" + ",".join(dq) + "]")


T = int(input())
solution(T)
