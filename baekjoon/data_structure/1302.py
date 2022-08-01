# https://www.acmicpc.net/problem/1302
# 베스트셀러
import sys

input = lambda: sys.stdin.readline().rstrip()

books = dict()
for _ in range(int(input())):
    title = input()
    if title not in books:
        books[title] = 1
    else:
        books[title] += 1

max_val = max(books.values())
ans = []
for k, v in books.items():
    if v == max_val:
        ans.append(k)

ans.sort()
print(ans[0])

