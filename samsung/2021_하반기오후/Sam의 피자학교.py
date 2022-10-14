dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dys, dxs = (-1, 0, 1, 0), (0, 1, 0, -1)


def put_flour():
    insert_dow = min(dow)
    for i in range(dow_number):
        if dow[i] == insert_dow:
            dow[i] += 1


def rotate(array):
    new_array = array[::-1]
    return list(zip(*new_array))


def roll_dow(new_dow):
    start_x, start_y, end_y, case = dow_number - 1, 0, 1, True
    while True:
        if dow_number - start_x > dow_number - end_y:
            break
        imsi_dow = []
        count = 0
        for x in range(start_x, dow_number):
            imsi_dow.append([])
            for y in range(start_y, end_y):
                imsi_dow[count].append(new_dow[x][y])
                new_dow[x][y] = 0
            count += 1
        imsi_dow = rotate(imsi_dow)
        for x, new_x in zip(range(dow_number - len(imsi_dow) - 1, dow_number - 1), range(len(imsi_dow))):
            for y, new_y in zip(range(end_y, end_y + len(imsi_dow[0])), range(len(imsi_dow[0]))):
                new_dow[x][y] = imsi_dow[new_x][new_y]
        start_y = end_y
        end_y += len(imsi_dow[0])
        if case:
            start_x -= 1
            case = False

        else:
            case = True


def roll_half(new_dow):
    stack, end_x, start_x, start_y, end_y, case = 0, dow_number - 1, dow_number - 1, 0, dow_number // 2, True
    for _ in range(2):
        imsi_dow = []
        count = 0
        for x in range(start_x, dow_number):
            imsi_dow.append([])
            for y in range(start_y, end_y):
                imsi_dow[count].append(new_dow[x][y])
                new_dow[x][y] = 0
            count += 1
        imsi_dow = rotate(imsi_dow)
        imsi_dow = rotate(imsi_dow)
        for x, new_x in zip(range(dow_number - len(imsi_dow) - stack - 1, end_x), range(len(imsi_dow))):
            for y, new_y in zip(range(end_y, end_y + len(imsi_dow[0])), range(len(imsi_dow[0]))):
                new_dow[x][y] = imsi_dow[new_x][new_y]
        stack += 1
        start_y = end_y
        end_y += (dow_number - end_y) // 2
        start_x = dow_number - 2
        end_x = dow_number - 1


def dow_pang_pang():
    visited = [[True] * dow_number for _ in range(dow_number)]
    current = [[0] * dow_number for _ in range(dow_number)]
    for x in range(dow_number):
        for y in range(dow_number):
            if dow[x][y] != 0:
                visited[x][y] = False
                for dx, dy in dir:
                    new_x, new_y = x + dx, y + dy
                    if -1 < new_x < dow_number and -1 < new_y < dow_number and dow[new_x][new_y] and visited[new_x][new_y]:
                        if dow[x][y] + 4 < dow[new_x][new_y]:
                            current[x][y] += (dow[new_x][new_y] - dow[x][y]) // 5
                            current[new_x][new_y] += (dow[new_x][new_y] - dow[x][y]) // 5 * -1
                        elif dow[new_x][new_y] + 4 < dow[x][y]:
                            current[x][y] += (dow[x][y] - dow[new_x][new_y]) // 5 * -1
                            current[new_x][new_y] += (dow[x][y] - dow[new_x][new_y]) // 5
    for x in range(dow_number):
        for y in range(dow_number):
            dow[x][y] += current[x][y]

    new_dow = [0] * dow_number
    i = 0
    for y in range(dow_number):
        for x in range(dow_number - 1, -1, -1):
            if dow[x][y]:
                new_dow[i] = dow[x][y]
                i += 1
    return new_dow


if __name__ == "__main__":
    dow_number, max_min_diff = map(int, input().split())
    dow = list(map(int, input().split()))
    count = 1
    while True:
        put_flour()
        new_dow = [[0] * dow_number for _ in range(dow_number)]
        for i in range(dow_number):
            new_dow[dow_number - 1][i] = dow[i]
        roll_dow(new_dow)
        dow = dow_pang_pang()
        new_dow = [[0] * dow_number for _ in range(dow_number)]
        for i in range(dow_number):
            new_dow[dow_number - 1][i] = dow[i]
        roll_half(new_dow)
        dow = dow_pang_pang()
        if max(dow) - min(dow) <= max_min_diff:
            print(count)
            break
        count += 1
