# 상하좌우의 거리는 x, y 좌표의 abs()로 구하기, 위치 정보가 정해져 있으면, 딕셔너리
def solution(numbers, hand):
    keypad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        '*': (3, 0),
        0: (3, 1),
        '#': (3, 2)
    }
    answer = ''
    left = (1, 4, 7)
    right = (3, 6, 9)
    cur_left = '*'
    cur_right = '#'

    for number in numbers:
        if number in left:
            answer += 'L'
            cur_left = number
        elif number in right:
            answer += 'R'
            cur_right = number
        else:
            '''
            cur_right = 3 -> 0, 2
            cur_left = 4 -> 1, 0
            number = 5 -> 1, 1
            '''
            r_x, r_y = keypad[cur_right]
            l_x, l_y = keypad[cur_left]
            x, y = keypad[number]
            dis_left = abs(l_x - x) + abs(l_y - y)
            dis_right = abs(r_x - x) + abs(r_y - y)
            if dis_left < dis_right:
                answer += 'L'
                cur_left = number
            elif dis_left > dis_right:
                answer += 'R'
                cur_right = number
            else:
                if hand == "left":
                    answer += 'L'
                    cur_left = number
                else:
                    answer += 'R'
                    cur_right = number
    return answer
