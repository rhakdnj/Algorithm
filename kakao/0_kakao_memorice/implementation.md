### 키패드 누르기

1. 좌표값을 저장하는 딕셔너리를 통해 구현
2. 

```python
def get_distance(hand, number):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    number = str(number)
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    return abs(x_hand - x_number) + abs(y_hand - y_number)

def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    hand = 'R' if hand == 'right' else 'L'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = str(number)
            continue
        if number in [3, 6, 9]:
            answer += 'R'
            right = str(number)
            continue
        if number in [2, 5, 8, 0]:
            dis1 = get_distance(left, number)
            dis2 = get_distance(right, number)
            if dis1 > dis2:
                answer += 'R'
                right = str(number)
            if dis1 < dis2:
                answer += 'L'
                left = str(number)
            if dis1 == dis2:
                answer += hand
                if hand == 'R':
                    right = str(number)
                if hand == 'L':
                    left = str(number)
    return answer
```

### 수식 최대화

1. re 모듈을 통해 구현 
2. re.split('([*+-])', expression) 

```python
from itertools import permutations
import re

def solution(expression):
    operators = list(permutations('*+-', 3))
    expression = re.split('([*+-])', expression)
    answer = []
    
    for operator in operators:
        exp = expression[:]
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                exp[idx - 1] = str(eval(exp[idx - 1] + op + exp[idx + 1]))
                del exp[idx: idx + 2]
        answer.append(abs(int(exp[0])))
    return max(answer)
```

```python

```