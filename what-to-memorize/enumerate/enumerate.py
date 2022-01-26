seasons = ['Spring', 'Summer', "Autumn", "Winter"]
# != [enumerate(seasons)] -> 형변환이 되지 않는다
arr = list(enumerate(seasons))
print(arr)

for idx, val in enumerate(seasons):
    print(idx, val)

arr2 = list(enumerate(seasons[1:], start=1))
for idx, val in arr2:
    print(idx, val)