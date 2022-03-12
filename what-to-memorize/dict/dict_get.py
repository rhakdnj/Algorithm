a = {'banana': 1000, "strawberry": 2000}

print(a.get('banana'))
print(a.get('strawberry'))
# None을 반환
print(a.get('apple'))
print(a.get('apple', 0))
