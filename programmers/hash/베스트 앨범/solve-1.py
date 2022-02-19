def solution(genres, plays):
    answer = []
    # genre : []
    d = {e: [] for e in set(genres)}
    # d[genre] = [[plays[i], i]]
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])

    # dict.keys() -> dict_keys 라는 타입(리스트가 아니다)
    genre_sort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)

    for g in genre_sort:
        # genre 내에서 play 횟수가 많은 순, 그리고 index 가 작은 순서
        temp = [e[1] for e in sorted(d[g], key=lambda x: (-x[0], x[1]))]
        # [:min(len(temp), 2)]
        answer += temp[:min(len(temp), 2)]
    return answer
