import re


print(re.findall('a', 'a'))
print(re.findall('a', 'aba'))
print(re.findall('a', 'baa'))
print(re.findall('aaa', 'aaaaa'))
print(re.findall('aaa', 'aaaaaa'))
print(re.findall('\d', '숫자123이 이렇게56 있다8'))
print(re.findall('\d+', '숫자123이 이렇게56 있다8'))


# ['a']
# ['a', 'a']
# ['a', 'a']
# ['aaa']
# ['aaa', 'aaa']
# ['1', '2', '3', '5', '6', '8']
# ['123', '56', '8']

exp = "100-200*300-500+20"
exp = re.split('([*+-])', exp)
print(exp)



def solution(files):
    print(files)
    print(sorted(files))
    # a = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    a = sorted(files, key=lambda file: int(re.findall('\d{1,5}', file)[0]))
    print(a)
    b = sorted(a, key=lambda file: re.split('\d+', file.lower())[0])
    print(b)
    return b


files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
solution(files)
