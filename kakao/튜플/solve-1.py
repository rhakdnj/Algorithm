def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))
    answer = list({num: 0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
    return answer
