def solution(array, commands):
    answer = []
    # i, j, k는 1부터 인덱스가 시작
    for i, j, k in commands:
        answer.append(sorted(array[i - 1: j])[k - 1])
    return answer