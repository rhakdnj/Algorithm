def impossible(res: set) -> bool:
    COL, ROW = 0, 1
    for x, y, a in res:
        # 기둥 일 때
        if a == COL:
            if y != 0 and (x - 1, y, ROW) not in res and \
                    (x, y - 1, COL) not in res and (x, y, ROW) not in res:
                return False
        else:
            if (x, y - 1, COL) not in res and (x + 1, y - 1, COL) not in res and \
                    not ((x - 1, y, ROW) in res and (x + 1, y, ROW) in res):
                return False
    return True


def solution(n, build_frame):
    res = set()
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:
            res.add(item)
            if impossible(res):
                res.remove(item)
        elif item in res:
            res.remove(item)
            if impossible(res):
                res.add(item)
    answer = map(list, res)
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


# 자릿수 맞춰주기
# f'{str(시간//60).zfill(2)}:{str(시간%60).zfill(2)}'
