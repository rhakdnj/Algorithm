n = int(input())
arr = [list(input()) for _ in range(n)]
ret = n * n

# bit: 경우의 수
for bit in range(1 << n):
    temp = [arr[i][:] for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            # 켜져 있는 행에 대해서 change
            for j in range(n):
                if temp[i][j] == 'H':
                    temp[i][j] = 'T'
                else:
                    temp[i][j] = 'H'

    sum_ = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if temp[j][i] == 'T':
                cnt += 1
        sum_ += min(cnt, n - cnt)

    ret = min(ret, sum_)

print(ret)

