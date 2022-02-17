def solution(participant, completion):
    for temp in completion:
        participant.remove(temp)
    return participant[0]