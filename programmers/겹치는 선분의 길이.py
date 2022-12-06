import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(lines: list[list]):
    answer = 0
    cnt = [0 for _ in range(201)]
    for line in lines:
        start, end = line[0], line[1]
        for idx in range(start + 100, end + 100):
            cnt[idx] += 1

    for i in cnt:
        if i > 1:
            answer += 1

    return answer


def solution_1(lines: list[list]):
    sets = [set(range(min(lst), max(lst))) for lst in lines]
    return len(sets[0].intersection(sets[1]) | sets[1] & sets[2] | sets[2] & sets[0])


if __name__ == '__main__':
    print(solution([[0, 5], [3, 9], [1, 10]]))
    print(solution_1([[0, 5], [3, 9], [1, 10]]))

"""
lines	                    result
[[0, 1], [2, 5], [3, 9]]	2
[[-1, 1], [1, 3], [3, 9]]	0
[[0, 5], [3, 9], [1, 10]]	8
"""
