from itertools import permutations
import re


def solution(expression):
    priorities = (list(permutations(['*', '-', '+'], 3)))
    expression = re.split('([*+-])', expression)
    result = []
    for priority in priorities:
        # *, -, +
        exp = expression[:]
        for operator in priority:
            while operator in exp:
                idx = exp.index(operator)
                exp[idx - 1] = str(eval(exp[idx - 1] + operator + exp[idx + 1]))
                del exp[idx: idx + 2]
        result.append(abs(int(exp[0])))

    return max(result)


print(solution("100-200*300-500+20"))
