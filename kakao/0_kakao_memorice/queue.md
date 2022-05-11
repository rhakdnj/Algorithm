### 캐시

```python
from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    
    if not cacheSize:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if not cache:
            cache.append(city)
            answer += 5
            continue

        if city in cache:
            if cache[0] == city:
                answer += 1
                continue
            else:
                answer += 1
                i = cache.index(city)
                cache = deque([cache[i]] + [x for x in cache if x != city])
        else:
            if len(cache) == cacheSize:
                cache.pop()
                cache.appendleft(city)
            else:
                cache.appendleft(city)
            answer += 5

    return answer
```