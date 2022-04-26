from collections import deque, defaultdict

n, k = map(int, input().split())
visited = [False] * 100001
counter = defaultdict(int)
q = deque([(n, 0)])

while q:
    cur, count = q.popleft()
    visited[cur] = True

    if cur == k:
        counter[count] += 1
    else:
        if 0 <= cur + 1 <= 100000 and not visited[cur + 1]:
            q.append((cur + 1, count + 1))
        if 0 <= cur - 1 <= 100000 and not visited[cur - 1]:
            q.append((cur - 1, count + 1))
        if 0 <= cur * 2 <= 100000 and not visited[cur * 2]:
            q.append((cur * 2, count + 1))

for key in counter.keys():
    if key:
        print(key)
        print(counter[key])
        break
