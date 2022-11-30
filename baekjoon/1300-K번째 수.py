"""
k의 범위 1~min(10^9, N^2)이므로 시간 복잡도가 N^2인 알고리즘은 사용할 수 없다.
따라서 이진 탐색을 사용해야 한다.

2차원 배열은 N행이 N의 배수로 구성되어 있다. 2차원 배열에서의 k번째 수는 k를 넘지 못한다.
따라서 2차원 배열의 1~k 번째 행안에 정답이 존재한다.
시작 인덱스를 1, 종료 인덱스를 k로 정한다.

예) n = 3, k = 7
[
    [1, 2, 3],  # 4 // 1 = 4 이지만 한 행의 크기가 3 이므로 3개
    [2, 4, 6],  # 4 // 2 = 2
    [3, 6, 9]   # 4 // 3 = 1
]

최초의 중앙값은 (1 + 7) // 2 = 4, 중앙값보다 작거나 같은 수의 갯수는 중앙값을 인덱스로 나눈 값이다.
단 나눈 값이 인덱스보다 크면 중앙값으로 정한다. -> min(mid //i, N)

이를 통해 중앙값 4는 6번째 수보다 큰 수가 될 수 없다는 것을 알 수 있다.

문제에서 주어진 k보다 작으므로 중앙값을 늘린다.

"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(n, k):
    start, end = 1, k
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(1, n + 1):
            cnt += min(mid // i, n)

        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

    print(answer)


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    solution(N, K)
