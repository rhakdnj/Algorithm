# https://www.acmicpc.net/problem/20365
N = int(input())
colors = input()
cnt = {'B': 0, 'R': 0}
cnt[colors[0]] += 1

for i in range(1, N):
    if colors[i] != colors[i - 1]:
        cnt[colors[i]] += 1
print(min(cnt['B'], cnt['R']) + 1)
