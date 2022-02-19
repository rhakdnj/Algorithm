def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

'''
Counter([kind for name, kind in clothes]) -> kind 값을 Counter 객체를 만들어라

reduce(function, iterable[, initial]) -> value
https://www.daleseo.com/python-functools-reduce/    
'''
items = []
items.sort(key=lambda x: (x[0], -x[1], x[2]))