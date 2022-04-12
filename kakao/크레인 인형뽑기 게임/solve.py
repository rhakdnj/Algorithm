# 문제 잘 읽자 solve-1 처럼 넣은 다음 [-1], [-2] 비교로 if 문 간략화
def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1]:
                item = board[j][i - 1]
                board[j][i - 1] = 0
                if stack:
                    if stack[-1] == item:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(item)
                else:
                    stack.append(item)
                break
    return answer
