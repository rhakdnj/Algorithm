import re


def solution(files):
    r = re.compile('([a-zA-Z- .]+)([0-9]+)')

    return sorted(files, key=lambda x: (r.findall(x)[0][0].lower(), int(r.findall(x)[0][1]), files.index(x)))
