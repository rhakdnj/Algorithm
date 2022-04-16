def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        result = ""
        temp1 = str(bin(arr1[i]))[2:]
        temp2 = str(bin(arr2[i]))[2:]
        while len(temp1) < n:
            temp1 = '0' + temp1
        while len(temp2) < n:
            temp2 = '0' + temp2
        for i in range(n):
            if temp1[i] == '0' and temp2[i] == '0':
                result += " "
            else:
                result += "#"
        answer.append(result)

    return answer
