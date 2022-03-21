n = int(input())
array = sorted([int(input()) for _ in range(n)], reverse=True)

print(" ".join(map(str, array)))


