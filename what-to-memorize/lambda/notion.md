# 출처: 
https://velog.io/@pm1100tm/Python-lambda-%EB%9E%8C%EB%8B%A4

## 람다식

- 람다 표현식이라고 하며 이름이 없는 함수, 즉 익명 함수이다.

- 람다 표현식의 본체에는 인라인 형식의 간단한 표현식만 올 수 있다.

- 주로 다른 함수의 인수(파라미터)로 넘겨줄 때 많이 사용된다.

```python
lambda x, y: x + y

# lambda : 키워드
# x, y : 람다식 안에서 사용될 파라미터
# x + y : 람다식 안의 처리 코드 (자동으로 리턴)
```

- 간단한 인라인 콜백함수를 만들거나, 함수 안에서 복잡한 처리를 할 수 없을 때 유용하다

```python
# 람다식으로 표현
lambdas = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4
]

for lambda_func in lambdas:
    print(lambda_func(2))


# 일반 함수로 하면?
def square(x):
    return x ** 2


def power_3(x):
    return x ** 3


def power_4(x):
    return x ** 4


powers = [square, power_3, power_4]

for f in powers:
    print(f(2))
```

### 람다 호출하기

```python
# 변수로 만들어서 호출하기
lam = lambda x, y: x + y
r = lam(1, 2)

print(r) # 3

# (lambda 매개변수들: 식)(인수들)
r = (lambda x, y: x + y)(1, 2)

print(r) # 3
```

### 함수의 인자로 람다식 넣기

```python
# 변수로 만들어서 인수로 넘기기
lam = lambda x, y: x + y

def print_xy(lam):
    result = lam
    print(result)

print_xy(lam(1, 2)) # 3


# 함수를 호출할 때 인자 값으로 람다식 넣기
def print_xy(func, hello):
    print(func(1, 2))
    print(hello)

print_xy((lambda x, y: x+y), "hello")
```

### 람다식의 대표적인 예는 map, filter 내장함수이다.

```python
# 변수로 만들어서 인수로 넘기기
# [2, 4, 6]
list(map(lambda x, y: x + y, [1, 2, 3], [1, 2, 3]))

# 루트의 정수부
# [1, 1, 1, 2, 2, 2, 2, 2, 3]
l = list(map(int, [i ** (1/2) for i in range(1, 10)]))

# plus_ten 리스트 
list(map(lambda x : x+10 ,[1, 2, 3])) 
```

### 람다식에서 조건문 사용하기

**람다 표현식 조건문 사용시 주의할 점**

- if else 조건문 사용시 :(콜론)을 붙히지 않음 

- if를 사용했다면 반드시 else도 사용해줘야한다. `if만 사용시 error`

- elif를 사용할 수 없다

**map 함수**

```python
#  map을 이용해 a라는 리스트에서 2의 배수를 문자열로 출력
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [1, '2', 3, '4', 5, '6', 7, '8', 9, '10']
list(map(lambda x : str(x) if x % 3 == 0 else x, a))

# 람다 표현식에 조건문 여러개 사용하기
# 1은 문자열로 변환하고, 2는 제곱수로 변환, 3 이상은 10을 더하는 식은 다음과 같이 작성
list(map(lambda x : str(x) if x== 1 else float(x) if x==2 else x+10,a))

# 결과
# ['1', 4, 13, 14, 15, 16, 17, 18, 19, 20]
```

**filter 함수**

```python
arr = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

result = list(filter(lambda x: 5 < x < 10, arr))

# 결과
# [8, 7, 9]
```

<br>

>사용 예시:
> 다음과 같이 비밀번호의 길이와 대문자가 포함된것을 확인하는 간단한 함수를 람다식으로 바꿔보자.

```python
lambdas = [
    lambda password: "SHORT_PASSWORD" if len(password) < 8 else None,
    lambda password: "NO_CAPITAL_LETTER_PASSWORD" if not any(c.isupper() for c in password) else None
]


def check_password_using_lambda(password):

    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True


print( check_password_using_lambda('123') )            # SHORT_PASSWORD
print( check_password_using_lambda('12356789f') )      # NO_CAPITAL_LETTER_PASSWORD
print( check_password_using_lambda('123456789fF') )    # True
```
