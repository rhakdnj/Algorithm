from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if not cacheSize:
        return len(cities) * 5

    for city in cities:
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
            answer += 5
            cache.appendleft(city)

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
