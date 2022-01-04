word = list(input())
answer = []
temp = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i]
        second = word[i:j]
        last = word[j:]
        first.reverse()
        second.reverse()
        last.reverse()
        temp.append(first + second + last)

for i in temp:
    answer.append(''.join(i))

print(sorted(answer)[0])






# for a in tmp:
#     answer.append(''.join(a))

# print(sorted(answer)[0])