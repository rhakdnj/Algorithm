def print_subsets(arr, n):
    for i in range(1 << n):
        print('{', end='')
        for j in range(n):
            # i 번째 원소가 존재하는 지 확인
            """
            2번째 원소가 있는지 확인
            0101 & (1 << 2) = 0101 & 0100 = 0100
            """
            if i & (1 << j):
                print(arr[j], end=' ')
        print('}')


set_data = ['A', 'B', 'C', 'D']

print_subsets(set_data, 4)
