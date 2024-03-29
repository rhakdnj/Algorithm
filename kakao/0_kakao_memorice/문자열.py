# 신규 아이디 추천
"""
if answer[0] == '.':
    if len(answer) > 1:
        answer = answer[1:]
    else:
        answer = '.'
if answer[-1] == '.':
    answer = answer[:-1]
"""

"""
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
"""

# 수식 최대화
"""
import re
from itertools import permutations

def solution(expression):
    operators = list(permutations('+-*', 3))
    expression = re.split('([-*+])', expression)

"50*6-3*2"
>>	['50', '*', '6', '-', '3', '*', '2']
"""

# 숫자 문자열과 영단어
"""
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
"""

# 크레인 인형뽑기 게임
"""
열을 고정하고 행을 내리면서 할 수 있음 
열을 바깥 for문에서 고정 
inner for문에서 행을 가변적으로 가져가면서 진행
"""

# k진수에서 소수 개수 구하기
"""
빈 문자열을 continue하는 상황
if not num:
    continue
또는 
if len(num):
num이 빈 문자열이 아닐 때 
"""

# 다트 게임
"""
문자열의 10을 한번에 묶는 방법

a = dartResult.replace('10', '.')
dart_result = [i if i != '.' else '10' for i in a]
"""

# 튜플
"""
def solution(s):
    # 리스트로 나옴
    s = eval(s.replace("{", "[").replace("}", "]"))
    print(type(s))
    answer = list({num: 0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
    return answer


solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
"""

# 방금 그곡
"""
각 음은 1분에 1개씩 재생된다. 

def replace_special(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f')\
            .replace('G#', 'g').replace('A#', 'a')

라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 
재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.

-> 정렬 조건
if m in result:
    answer.append((name, play_time, cnt))
    cnt += 1

sorted(answer, key=lambda x: (-x[1], x[2]))[0][0]    
"""

# 압축
"""
dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))
"""

# 파일명 정렬(re)
"""

"""