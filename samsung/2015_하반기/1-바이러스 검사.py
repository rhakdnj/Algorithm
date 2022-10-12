n = int(input())
cust = list(map(int, input().split()))
cnt_ldr, cnt_mbr = map(int, input().split())
ans = 0

for cnt in cust:
    cnt -= cnt_ldr
    if cnt > 0:
        div, mod = divmod(cnt, cnt_mbr)
        ans += div
        if mod != 0:
            ans += 1
    ans += 1
print(ans)
