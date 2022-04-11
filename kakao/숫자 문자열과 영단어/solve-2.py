def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, v in enumerate(words):
        s = s.replace(words[i], str(i))

    return int(s)
