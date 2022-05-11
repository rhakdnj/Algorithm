### 길 찾기 게임

1. import sys -> solution 시작에 재귀 횟수 늘리기

```python
import sys


class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other):
        if (self.y == other.y):
            return self.x < other.x
        return self.y > other.y


def add_node(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            add_node(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            add_node(parent.right, child)


def preorder(ans, node):
    if node is None:
        return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)


def postorder(ans, node):
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)


def solution(nodeinfo):
    sys.setrecursionlimit(1500)
    size = len(nodeinfo)
    node_list = []
    for i in range(size):
        node_list.append(Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]))
    node_list.sort()
    root = node_list[0]
    for i in range(1, size):
        add_node(root, node_list[i])

    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))


```

### 표 편집

```python
class Node:
    def __init__(self):
        self.deleted = False
        self.prev = None
        self.next = None


def solution(n, k, cmd: str):
    node_arr = [Node() for _ in range(n)]
    for i in range(1, n):
        node_arr[i].prev = node_arr[i - 1]
        node_arr[i - 1].next = node_arr[i]

    cur = node_arr[k]
    stack = []
    for s in cmd:
        if s.startswith('U'):
            m = int(s[2:])
            for _ in range(m):
                cur = cur.prev
        elif s.startswith('D'):
            m = int(s[2:])
            for _ in range(m):
                cur = cur.next
        elif s == 'C':
            stack.append(cur)
            cur.deleted = True
            up, down = cur.prev, cur.next
            if up:
                up.next = down
            if down:
                down.prev = up
                cur = down
            else:
                cur = up
        else:
            node = stack.pop()
            node.deleted = False
            up, down = node.prev, node.next
            if up:
                up.next = node
            if down:
                down.prev = node

    answer = ''
    for node in node_arr:
        if node.deleted:
            answer += 'X'
        else:
            answer += 'O'
    return answer

```