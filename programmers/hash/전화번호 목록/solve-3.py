import re


def solution(phone_book):
    for b in phone_book:
        p = re.compile("^"+b)
        for b2 in phone_book:
            if b != b2 and p.match(b2):
                return False
    return True


phone_book = ["12", "123", "1235", "567", "88", "9123"]
print(solution(phone_book))
