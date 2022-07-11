from collections import defaultdict
from math import ceil


def solution(n, words):
    answer = [0, 0]
    last_word = None
    count = 0
    word_dict = defaultdict(int)
    for word in words:
        count += 1
        word_dict[word] += 1
        if last_word is None:
            last_word = word[-1]
            continue
        if last_word != word[0] or word_dict[word] == 2:
            answer[0] = count % n if count % n else n
            answer[1] = ceil(count / n)
            break
        last_word = word[-1]
    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

