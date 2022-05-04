"""
속성이 8이하 이기 때문에, bit로 표현하는 것

bit로 후보키를 mapping 할 수 있다.

유일성을 통해 후보키의 후보를 구하고, 만족한 후보들을 최소성으로 후보키를 구한다.
"""

from functools import cmp_to_key


def compare(a, b):
    x = bin(a).count('1')
    y = bin(b).count('1')
    return x - y


def check(relation: list, row_size, col_size, subset):
    for a in range(row_size - 1):
        for b in range(a + 1, row_size):
            is_same = True
            for k in range(col_size):
                if (subset & 1 << k) == 0:
                    continue
                if relation[a][k] != relation[b][k]:
                    is_same = False
                    break
            if is_same:
                return False
    return True


def solution(relation: list):
    answer = 0
    row_size = len(relation)
    col_size = len(relation[0])
    candidates = []

    for i in range(1, 1 << col_size):
        if distance(relation, row_size, col_size, i):
            candidates.append(i)

    candidates = sorted(candidates, key=cmp_to_key(compare))

    while len(candidates) != 0:
        n = candidates.pop(0)
        answer += 1
        candidates = [x for x in candidates if (n & x) != n]

    return answer
