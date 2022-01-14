import sys
input = sys.stdin.readline

arr = [input().rstrip() for _ in range(36)]

if len(set(arr)) == 36:
    for i in range(35):
        if abs((ord(arr[i][0]) - ord(arr[i+1][0])) * (int(arr[i][1]) - int(arr[i+1][1]) ) ) != 2:
            print("Invalid")
            break
    else:
        if abs((ord(arr[-1][0]) - ord(arr[0][0]) ) * (int(arr[-1][1]) - int(arr[0][1]) ) ) != 2:
            print("Invalid")
        else:
            print("Valid")
else:
    print("Invalid")











# arr = [input().rstrip() for _ in range(36)]

# visited = [[False for _ in range(6)] for _ in range(6)]


# for i in range(36):
#     row = ord(arr[i][0]) - ord('A')
#     col = int(arr[i][1]) - 1
#     if visited[row][col] == True:
#         print("Invalid")
#         exit()
#     else:
#         visited[row][col] = True

# if abs((ord(arr[-1][0]) - ord(arr[0][0]) ) * (int(arr[-1][1]) - int(arr[0][1]) ) ) != 2:
#     print("Invalid")
# else:
#     print("Valid")

