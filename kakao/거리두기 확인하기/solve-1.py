'''
그래프에서 i, j 의 값과 graph[i][j]를 다 사용해야하는 경우이면 enumerate도 좋은 생각이다.
그리고 안되는 경우만 생각하는 것도
'''


def check(place: list):
    for i, row in enumerate(place):
        for j, ceil, in enumerate(row):
            if ceil != 'P':
                continue
            if i != 4 and place[i + 1][j] == 'P':
                return 0
            if j != 4 and place[i][j + 1] == 'P':
                return 0
            if i < 3 and place[i + 2][j] == 'P' and place[i + 1][j] != 'X':
                return 0
            if j < 3 and place[i][j + 2] == 'P' and place[i][j + 1] != 'X':
                return 0
            if i != 4 and j != 4 and place[i + 1][j + 1] == 'P' and (
                    place[i + 1][j] != 'X' or place[i][j + 1] != 'X'):
                return 0
            if i != 4 and j != 0 and place[i + 1][j - 1] == 'P' and (
                    place[i + 1][j] != 'X' or place[i][j - 1] != 'X'):
                return 0
    return 1


def solution(places):
    return [check(place) for place in places]
