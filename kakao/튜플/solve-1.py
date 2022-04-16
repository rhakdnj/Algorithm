def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))
    answer = list({num: 0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
