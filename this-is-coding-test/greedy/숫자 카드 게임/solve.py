n, m = map(int, input().split())
cards = [min(map(int, input().split())) for _ in range(n)]

print(max(cards))
