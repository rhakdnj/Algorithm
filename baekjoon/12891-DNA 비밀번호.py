s, p = map(int, input().split())
dna_str = input()
dna_cnt = [0 for _ in range(4)]
# 'A', 'C', 'G', 'T'
strong_cnt = list(map(int, input().split()))
dna_index_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
secret_cnt = 0
answer = 0


def remove(ch: str):
    global secret_cnt
    index = dna_index_dict[ch]
    if dna_cnt[index] == strong_cnt[index]:
        secret_cnt -= 1
    dna_cnt[index] -= 1


def add(char: str):
    global secret_cnt
    index = dna_index_dict[char]
    dna_cnt[index] += 1
    if dna_cnt[index] == strong_cnt[index]:
        secret_cnt += 1


def check():
    global answer
    if secret_cnt == 4:
        answer += 1


def solution():
    global secret_cnt

    for val in strong_cnt:
        if val == 0:
            secret_cnt += 1

    for i in range(p):
        add(dna_str[i])
    check()

    for i in range(p, s):
        add(dna_str[i])
        remove(dna_str[i - p])
        check()

    print(answer)


solution()
