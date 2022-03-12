from collections import deque

# 빈 queue
queue1 = deque()

# 원소가 있는 queue 만들기
queue2 = deque([1, 2, 3])

# 큐 최대 길이 명시하기(원소를 이 보다 더 많이 넣으면 자동 갱신)
queue3 = deque(maxlen=5)

# queue에 원소를 넣으려면 append 메서드
queue4 = deque()
queue4.append(5)
print(queue4)

while queue2:
    print("{}을 pop했습니다.".format(queue2.popleft()))

