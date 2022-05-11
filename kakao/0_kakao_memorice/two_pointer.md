### 보석 쇼핑

1. gems 배열의 길이가 탐색 알고리즘은 O(n^2)이기에 힘들다
2. O(n) 투 포인터 알고리즘으로
3. 딕셔너리로 모든 종류 보석을 포함하는 구간

```python
from collections import defaultdict


def solution(gems):
    candidates = []
    start, end = 0, 0
    gems_len, gems_kind = len(gems), len(set(gems))
    gems_dict = defaultdict(int)

    while True:
        kind = len(gems_dict)
        if start == gems_len:
            break
        if kind == gems_kind:
            candidates.append((start, end))
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue
        if end == gems_len:
            break
        if kind != gems_kind:
            gems_dict[gems[end]] += 1
            end += 1
            continue

    answer = [0 , 0]
    shortest_len = 1000001
    for s, e in candidates:
        if shortest_len > e - s:
            shortest_len = e - s
            answer[0] = s + 1
            answer[1] = e
    return answer
```


### 징검 다리 건너기

1. stones 배열의 크기는 1 이상 200,000 이하입니다.(완전탐색은 빅오 초과)
2. 이진탐색으로 mid값을 구하고 체크(줄어드는 숫자가 완탐:1 , 더 빠름)
3. left == right일 때 while문에서 나옴

```python
def solution(stones, k):
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left
```