def solution(n, lost, reserve):
    set_reserve = [r for r in reserve if r not in lost]
    set_lost = [l for l in lost if l not in reserve]

    for r in set_reserve:
        if r - 1 in set_lost:
            set_lost.remove(r - 1)
        elif r + 1 in set_lost:
            set_lost.remove(r + 1)

    return n - len(set_lost)
