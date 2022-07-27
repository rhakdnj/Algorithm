# https://www.acmicpc.net/problem/18406
# 럭키 스트레이트
import sys

input = lambda: sys.stdin.readline().rstrip()

n = input()
n1, n2 = n[:len(n) // 2], n[len(n) // 2:]

sum1, sum2 = sum(map(int, n1)), sum(map(int, n2))

print('LUCKY') if sum1 == sum2 else print('READY')


def solution(s: str):
    length = len(s)
    summary = 0
    # 왼쪽 부분 자릿수 합 더하기
    for i in range(length // 2):
        summary += int(s[i])
    # 오른쪽 부분 자릿수 합 빼기
    for i in range(length // 2, length):
        summary -= int(s[i])

    print('LUCKY') if sum1 == sum2 else print('READY')
