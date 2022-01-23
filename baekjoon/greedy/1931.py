import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
meeting = [tuple((map(int, input().split())))for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))
res = 1
end_time = meeting[0][1]

for i in range(1, len(meeting)):
    if end_time <= meeting[i][0]:
        end_time = meeting[i][1]
        res += 1
else:
    print(res)






'''
11
0 6
1 4
2 13
3 5 
3 8
5 7
5 9
6 10
8 11
8 12
12 14



'''