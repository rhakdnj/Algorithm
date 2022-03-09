def solution(begin, target, words):
    answer = 0
    queue = [begin]

    while True:
        temp_q = []

