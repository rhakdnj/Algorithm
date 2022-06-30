def solution(s):
    arr = [chr(i) * 2 for i in range(ord('a'), ord('z') + 1)]
    answer = -1
    flag = True

    while flag and s:
        before = len(s)
        for i in arr:
            if i in s:
                s = s.replace(i, '')

        if before == len(s):
            return 0

    return 1
