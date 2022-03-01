def solution(brown, yellow):
    width = brown + yellow
    for col in range(3, int(width ** 0.5) + 1):
        if width % col == 0 and 2 * (width // col + col - 2) == brown:
            return [width // col, col]
