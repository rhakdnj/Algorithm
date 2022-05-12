from collections import defaultdict, deque
from copy import deepcopy
from itertools import permutations

Card_dict = defaultdict(list)
answer = 0

def bfs(board, start, end):
    if start == end: return 0
    queue, visit = deque([[start[0], start[1], 0]]), {start}
    while queue:
        x, y, c = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            cx, cy = x, y
            while True:
                cx, cy = cx + dx, cy + dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx - dx, cy - dy
                    break
                elif board[cx][cy] != 0:
                    break
            if (nx, ny) == end or (cx, cy) == end:
                return c + 1
            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c + 1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                queue.append((cx, cy, c + 1))
                visit.add((cx, cy))


def min_cost(board, curr, order, cost):
    # 모든 카드를 확인한 경우
    if len(order) == 0: return cost
    idx = order[0] + 1

    if answer >= cost:
        return

    # 현재 위치에서 A1까지의 조작 횟수 + A1 -> A2까지의 조작 횟수 + 2(Enter)
    choice1 = bfs(board, curr, Card_dict[idx][0]) + bfs(board, Card_dict[idx][0], Card_dict[idx][1]) + 2
    choice2 = bfs(board, curr, Card_dict[idx][1]) + bfs(board, Card_dict[idx][1], Card_dict[idx][0]) + 2

    # 선택한 카드는 Board 에서 0으로 변경
    new_board = deepcopy(board)
    new_board[Card_dict[idx][0][0]][Card_dict[idx][0][1]] = 0
    new_board[Card_dict[idx][0][1]][Card_dict[idx][0][0]] = 0

    if choice1 < choice2:
        return min_cost(new_board, Card_dict[idx][1], order[1:], cost + choice1)
    else:
        return min_cost(new_board, Card_dict[idx][0], order[1:], cost + choice2)


def solution(board, r, c):
    global Card_dict , answer
    answer = float('inf')
    for row in range(4):
        for col in range(4):
            num = board[row][col]
            if num:
                Card_dict[num].append((row, col))

    # 완전 탐색
    for case in permutations(range(len(Card_dict)), len(Card_dict)):
        answer = min(answer, min_cost(board, (r, c), case, 0))

    return answer