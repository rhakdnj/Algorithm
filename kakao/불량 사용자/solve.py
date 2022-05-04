from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(users[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            elif banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    p = permutations(user_id, len(banned_id))

    for users in p:
        if not distance(users, banned_id):
            continue
        else:
            users = set(users)
            if users in answer:
                continue
            answer.append(users)

    return len(answer)
