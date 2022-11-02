def solution():
    global answer

    start, end = 0, 0
    while end < n:
        if cnt_list[li[end]] == 0:
            cnt_list[li[end]] += 1
            end += 1
        else:
            answer += (end - start)
            cnt_list[li[start]] -= 1
            start += 1

    answer += ((end - start) * (end - start + 1)) // 2


if __name__ == '__main__':
    n = int(input())
    li = list(map(int, input().split()))
    cnt_list = [0 for _ in range(max(li) + 1)]
    answer = 0
    solution()
    print(answer)
