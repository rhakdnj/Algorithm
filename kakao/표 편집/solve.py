class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    node_arr = [Node() for _ in range(n)]
    for i in range(1, n):
        node_arr[i - 1].next = node_arr[i]
        node_arr[i].prev = node_arr[i - 1]

    cur = node_arr[k]
    stack = []

    for str in cmd:
        if str[0] == 'U':
            x = int(str[2:])
            for _ in range(x):
                cur = cur.prev
        elif str[0] == 'D':
            x = int(str[2:])
            for _ in range(x):
                cur = cur.next
        elif str[0] == 'C':
            stack.append(cur)
            cur.removed = True
            up = cur.prev
            down = cur.next
            if up:
                up.next = down
            if down:
                down.prev = up
                cur = down
            else:
                cur = up
        else:
            node = stack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node

    answer = ''
    for i in range(n):
        if node_arr[i].removed:
            answer += 'X'
        else:
            answer += 'O'
    return answer