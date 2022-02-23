from collections import deque

priorities = [6, 1, 3, 2]

queue = deque([i, v] for i, v in enumerate(priorities))

print(max(queue, key=lambda x: x[1]))
