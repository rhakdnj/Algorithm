def solution(places):
    answer = []
    for place in places:
        p_list = []
        status = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_list.append((i, j))

        for k in range(len(p_list) - 1):
            if not status:
                break
            k_x, k_y = p_list[k]
            for l in range(k + 1, len(p_list)):
                l_x, l_y = p_list[l]
                if abs(k_x - l_x) + abs(k_y - l_y) == 1:
                    answer.append(0)
                    status = False
                    break
                elif abs(k_x - l_x) + abs(k_y - l_y) == 2:
                    if k_x - l_x == -2:
                        if place[k_x + 1][k_y] == 'O':
                            answer.append(0)
                            status = False
                            break
                    elif k_y - l_y == -2:
                        if place[k_x][k_y + 1] == 'O':
                            answer.append(0)
                            status = False
                            break
                    elif k_x - l_x == -1 and k_y - l_y == -1:
                        if place[k_x + 1][k_y] == 'O' or place[k_x][k_y + 1] == 'O':
                            answer.append(0)
                            status = False
                            break
                    else:
                        if place[k_x + 1][k_y] == 'O' or place[k_x][k_y - 1] == 'O':
                            answer.append(0)
                            status = False
                            break
        if status:
            answer.append(1)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
'''
대기실 5 개 
각 대기실의 크기 5 * 5
거리두기 = 맨허튼 거리 > 2

예외)
맨허튼 거리 < 2
파티션 -> ok


0, 0
0, 4
2, 1
4, 1
4, 4


'''
