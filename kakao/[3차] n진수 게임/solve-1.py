def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0"
    for number in range(1, t * m):
        temp = []
        while number > 0:
            temp.append(data[number % n])
            number //= n
        numbers += "".join(reversed(temp))

    return numbers[p - 1:t * m:m]
