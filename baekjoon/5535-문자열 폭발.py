if __name__ == '__main__':
    string = input()
    target = input()

    stack = []
    for ch in string:
        stack.append(ch)
        if ch == target[-1] and ''.join(stack[-len(target):]) == target:
            del stack[-len(target):]

    answer = ''.join(stack)

    if len(answer):
        print(answer)
    else:
        print('FRULA')
